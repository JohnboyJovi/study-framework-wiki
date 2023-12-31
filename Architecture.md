# A list of classes that potentially are of interest for study developers

The classes are in principle divided in those used for setting up and those used at runtime

## Setup Phase Classes

* ``ASFStudySetup``: An actor holding the entire setup, that is synced with a json file (at saving the map the json file is written and loaded at startup, so you could change the json while the Unreal Editor is not running and your changes are preserved). A study has different phases:
* ``USFStudyPhase``: A phase has a name and different factors and dependent variables, it can also be used to have a warm-up scene or a nice end/farewell/thank-you scene
* ``USFStudyFactor``: Represents a factor you want to examine in the study with different levels. Multiple factors can exist. 
  * ``USFMapFactor``: This is a child class representing the level/map that should be shown. At least one ``USFMapFactor``with one map needs to be specified per phase!
* ``USFDependentVariable``: This represents dependent variables you want to measure per condition (combination of levels of your factors). All values are gathered as strings. No dependent variable is required. Time of each condition is anyways always logged.
  * ``USFMultipleTrialDependentVariable``: These are sepcial dependent variable which should gather data for multiple trial during one condition, so not just a single value per condition.
* ``USFIndependentVariable``: This represents independent variables you want to measure for a whole study run of one participant. All values are gathered as strings. The variables can be asked at the beginning of the study run for each participant automatically.

## Study Execution Classes

* ``USFGameInstance``: This is the central interface during execution, you can get it via: ``USFGameInstance::Get()``
* ``USFParticipant``: The participant used to store its data at runtime, participants are numbered, using increasing integers for better controllability
* ``USFCondition``: the actual condition (combination of factor levels) used at runtime for storing data etc.

