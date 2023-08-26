# This script can reconstruct phase tables with missing data from the participant logs
# Prerequsites:
#  - The headers of the phase tables need to be valid (apart from those the files can be empty)
#  - the IndependentVariables.csv needs to be complete (we just assume this since it was the case for us, otherwise also restore that!)
#  - no underscore (_) in the Phase or multi trial variable names

import os
from contextlib import chdir

FolderToLogs = "StudyLogs/ParticipantLogs"
FolderToPhaseTables = "StudyLogs"

IndependentVars = {}

def LoadIndependentVars():
    global IndependentVars
    ConvertCoding(os.path.join(FolderToPhaseTables, "IndependentVariables.csv"))
    with open(os.path.join(FolderToPhaseTables, "IndependentVariables.csv"), 'r') as file:
        header_entries = []
        for line in file:
            if len(header_entries) == 0:
                header_entries = line.strip().split(",")
                continue
            entries = line.strip().split(",")
            data = {}
            for i in range(0, len(entries)):
                data[header_entries[i]] = entries[i]
            IndependentVars[entries[0]] = data
    #print(IndependentVars)

def CreateEntryLine(header_entries, data):
    line = ""
    for entry in header_entries:
        if entry in data:
            line += data[entry]
        else:
            if not (entry == "lowerPrio" or entry == "higerPrio"):
                #some vars are not required (which we don't know here, so I added them for our case manually!)
                print("WARNING: Missing data for "+entry)
        if not entry == header_entries[-1]:
            line += ","
        else:
            line += "\n"
    return line

def CheckForSplitCommaInSentence(entries):
    entries_cleaned = []
    i=0
    while i < len(entries):
        if entries[i].startswith("\"") and not entries[i].endswith("\""):
            cleaned_entry = ""
            while not entries[i].endswith("\""):
                cleaned_entry += entries[i] + "[Komma]"
                i += 1
            cleaned_entry += entries[i]
            entries_cleaned.append(cleaned_entry)
        else:
            entries_cleaned.append(entries[i])
        i += 1
    return entries_cleaned

def RecoverDataTable(phase_filename, multi_trial):
    phase_name = phase_filename.replace("Phase_","").replace(".csv","")
    multi_trial_var_name = ""
    if multi_trial:
        phase_name = phase_filename.replace(".csv","").split("_")[1]
        multi_trial_var_name = phase_filename.replace(".csv","").split("_")[2]
    header_entries = []
    out_lines = []
    #read in header of this table
    with open(os.path.join(FolderToPhaseTables, phase_filename), 'r') as f:
        header_line = f.readline()
        header_entries = header_line.strip().split(",")
        out_lines.append(header_line)

    #now read through all participant logs and gather relevant information
    with chdir(FolderToLogs):
        for filename in sorted(filter(os.path.isfile, os.listdir(".")), key=os.path.getmtime):
            with open(filename, 'r') as file:
                ParticipantID = filename.split("-")[1].split("_")[0]
                reading_relevant_condition = False
                trial_nr = 0
                start_time = 0.0
                data = {}
                for line in file:
                    if "Start Condition:" in line and "Phase: "+phase_name+";" in line:
                        reading_relevant_condition = True
                        trial_nr = 0 #simply not used if not multi-trial var
                        start_time = float(line.strip().replace("#","").split(":")[0])
                        data = {"Phase":phase_name}
                        data.update(IndependentVars[ParticipantID]) # adds ParticipantId and IVs to dict
                        for factor_levels in line.split("(")[1].split(")")[0].split(";"):
                            if "Phase:" in factor_levels:
                                continue
                            factor, level = factor_levels[1:].split(": ")
                            data[factor] = level
                    if reading_relevant_condition and "EndCondition" in line:
                        reading_relevant_condition = False
                        if not multi_trial:
                            #in multi_trial case we store data not at the end but when it is recorded
                            data["Time"] = "{:.2f}".format(float(line.strip().replace("#","").split(":")[0]) - start_time)
                            out_lines.append(CreateEntryLine(header_entries, data))
                            #print(line)
                    if "Recorded" in line:
                        var_name = line.split(" ")[2][:-1] #last part removes ":" from the end
                        var_value = line.strip().split(" ",3)[3]
                        if multi_trial and var_name == multi_trial_var_name and reading_relevant_condition:
                            #this is a multi trial var we are looking for
                            var_entries = var_value.replace("{","").replace("}","").split(",")
                            #maybe we split at , in phrases which are escaped in ", so check that!
                            var_entries = CheckForSplitCommaInSentence(var_entries)
                            for i in range(0,len(var_entries)):
                                header_index = len(header_entries)-len(var_entries)+i
                                data[header_entries[header_index]] = var_entries[i]
                            data["Trial"] = str(trial_nr)
                            trial_nr += 1
                            out_lines.append(CreateEntryLine(header_entries, data))
                        if (not multi_trial) and var_name in header_entries:
                            data[var_name] = var_value
    #now write this
    if not os.path.exists(os.path.join(FolderToPhaseTables,"Recovered")):
        os.mkdir(os.path.join(FolderToPhaseTables,"Recovered"))
    with open(os.path.join(FolderToPhaseTables,"Recovered",phase_filename), 'w') as f:
        f.writelines(out_lines)



def ConvertCoding(full_filename):
    #remove all the byte order marks that Unreal puts in there
    with open(full_filename, mode='r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        modified_lines = [line.lstrip('\ufeff') for line in lines]
    with open(full_filename, mode='w', encoding='utf-8') as file:
        file.writelines(modified_lines)


def Main():
    LoadIndependentVars()
    #go through all files in the phasetable folder
    for filename in os.listdir(FolderToPhaseTables):
        if filename.startswith("Phase") and filename.endswith(".csv"): 
            #if not filename == "Phase_Decision_singlePlayDurationLeft.csv":
            #    continue
            full_name = os.path.join(FolderToPhaseTables, filename)
            ConvertCoding(full_name)
            print(full_name)
            #check whether this is a multiple trial data table or a normal phase
            with open(full_name, 'r') as f:
                header = f.readline()
                if ",Trial," in header:
                    #we expect this to be a multiple trial data table
                    RecoverDataTable(filename, True)
                else:
                    RecoverDataTable(filename, False)



Main()