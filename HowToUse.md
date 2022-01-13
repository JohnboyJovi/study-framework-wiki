# How to use the Study Framework to setup your own factorial study in Unreal

* First of all get the StudyFramework as Plugin into you project, e.g., using the setup script of the [RWTH VR Project Template](https://devhub.vr.rwth-aachen.de/VR-Group/unreal-development/unrealprojecttemplate), this plugin also requires the following plugins:
  * [``RWTH VR Toolkit``](https://devhub.vr.rwth-aachen.de/VR-Group/unreal-development/plugins/rwth-vr-toolkit)
  * [``Universal Logging``](https://devhub.vr.rwth-aachen.de/VR-Group/unreal-development/plugins/universallogging)
* This framework requires a Setup map (e.g., simply the Main level) which is started and contains a study setup, but is not part of the study itself. Add a SFStudySetup (``StudyFrameworkPlugin C++ Classes -> StudyFrameworkPlugin -> Public -> SFStudySetup``) actor to this level. In the properties section of this actor we can set up the study (which is also on saving the map stored in a json file, which chan be changed and is reloaded on editor start. Furthermore there are buttons to storing into and loading from a json file specified, which will be searches in ``ProjectDir/StudyFramework``).
* Add phases to this setup\
 ![image](uploads/06e2902e6cda1d9dc7994f03ff937145/image.png)\
and select ``SFStudyPhase`` instead of ``None`` (phases can be used if some blocks of the study should always come in the same order, e.g., always start with a warm-up phase or always end with a nice end scene), at least one phase needs to be present!
* Open the phase's details (1) and give it a recognizable name, then add a factor (2)\
![image](uploads/d02708b9b1c4ba267fce27c25ad09564/image.png)\
Factors define the different conditions you want to examine, e.g., in a 2x2 factorial design you have two factors with two levels each giving 4 conditions in total to examine. There are currently two kinds of factors to chose from:
  * ``SFMapFactor`` specifying which map/maps to use. Exactly one map factor has to be present per phase with at least one level.
  * ``SFStudyFactor`` to specify any other factor you want to examine, giving all the levels 
* .. configure factors (hint to [randomization](Randomization))
* .. configure dependents
* .. set game instance (Setting -> Project Setting -> Maps&Modes) Set to SFGameInstance
* .. set game mode (Setting -> Project Setting -> Maps&Modes) Set to SFGameMode

:warning: So far only notes!

* Setup with c++ or actor? --> rather only blueprint (and json)
* Interfacing with USFGameInstance (progressing, getting levels)
* what factors and randomness exists?
