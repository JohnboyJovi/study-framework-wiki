# How to use the Study Framework to setup your own factorial study in Unreal

* First of all get the StudyFramework as Plugin into you project, e.g., using the setup script of the [RWTH VR Project Template](https://devhub.vr.rwth-aachen.de/VR-Group/unreal-development/unrealprojecttemplate)
* This framework requires a Setup map (e.g., simply the Main level) which is started and contains a study setup, but is not part of the study itself. Then add a SFStudySetup (``StudyFramePlugin C++ -> Public -> SFStudySetup``) actor to this level. In the properties section of this actor we can set up the study (which is also on saving the map stored in a json file, which chan be changed and is reloaded on editor start).
* Add phases to this setup :x: 
(phases can be used if some blocks of the study should always come in the same order, e.g., always start with a warm-up phase or always end with a nice end scene), at least one phase needs to be present!
* .. configure factors (hint to [randomization](Randomization))
* .. configure dependents
* .. set game instance (Setting -> Project Setting -> Maps&Modes) Set to SFGameInstance
* .. set game mode (Setting -> Project Setting -> Maps&Modes) Set to SFGameMode

:warning: So far only notes!

* Setup with c++ or actor? --> rather only blueprint (and json)
* Interfacing with USFGameInstance (progressing, getting levels)
* what factors and randomness exists?
