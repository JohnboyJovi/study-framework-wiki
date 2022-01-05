# A list of classes that potentially are of interest for study developers

The classes are in principle divided in those used for setting up and those used at runtime

## Setup phase

* ``ASFStudySetup``: An actor holding the entire setup, that is synced with a json file (at saving the map the json file is written and loaded at startup, so you could change the json while the Unreal Editor is not running and your changes are preserved). A study has different phases:
* ``USFStudyPhase``: A phase has a name and different factors and dependent variables, it can also be used to have a warm-up scene or a nice end/farewill/thank-you scene
* ``USFStudyFactor``: Represents a factor you want to examine in the study with different levels. It can exists multiple factors. ``USFMapFactor`` is a child class representing the level/map that should be shown. At least one USFMApFactor with one level needs to be specified per phase!
* ``USFDependentVariable``: This represents dependent variables you want to measure per condition (combination of levels of your factors). All values are gathered as strings.

# Study Execution

* ``USFGameInstance``: This is the central interface during execution, you can get it via: ``USFGameInstance::Get()``
* ``USFParticipant``: The participant used to store its data at runtime, participants are numbered, using increasing integers for better controllability
* ``USFCondition``: the actual condition (combination of factor levels) used at runtime for storing data etc.

