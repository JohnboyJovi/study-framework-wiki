# What is logged and where:

* In `StudyFramework/StudyLogs/Phase_[PhaseName].csv` holds for each phase the data of all participants. This is in a format to easily use in statistics tool like *r*.
* In `StudyFramework/StudyLogs/Phase_[PhaseName]_[MultiTrialDependentVarName].csv` likewise all data collected for this ``USFMultipleTrialDependentVariable`` in this phase is stored in a similar format
* both of the above also store for each collected value the phase, factor level and independent variable to facilitate usage in statistics software such as *r* 
* In `StudyFramework/StudyLogs/IndependentVariables.csv`, all asked for independent variables per participant are stored.
* In `StudyFramework/StudyLogs/ParticipantLogs/LogParticipant-[i]` comments (with a preceeding '#'), events (Start condition..) and reported dependent variable values are logged
* In `StudyFramework/StudyLogs/PositionLogs/PositionLogParticipant-[i]` the position & rotation info of tracked actors/components are logged
* In `StudyFramework/StudyRuns/LastParticipant.txt` always the last participant that the study was executed and some information on that run is stored.
* In `StudyFramework/StudyRuns/Participant_[i].txt` the conditions planned/executed for participant i are stored as json.
* In `StudyFramework/DebuggingLogs/SFLog.txt` all logs generated by the study framework in the last run of Unreal are gathered (mainly for debugging).

# Recording Data

* You can record events happening during the execution (such as interactions done by the participant etc.) using 
  * ``USFGameInstance::Get()->LogComment(Comment, bAlsoLogToHUD)``
  * ``SFLoggingBPLibrary::LogComment(Comment, bAlsoLogToHUD)`` (easier to call within a blueprint)
* You can record data for the dependent variable specified using
  * ``USFGameInstance::Get()->LogData(DependentVarName, Value)`` or
  * ``USFLoggingBPLibrary::LogData(DependentVariableName, Value)`` (easier to call within a blueprint) 
  * :warning: you can call this multiple times in one condition which will overwrite the previous value. Only one value per condition can be stored in the phase long tables, so make sure that you combine values into one string if you for example want to store multiple reaction times in one condition.
* You can record data for the multiple trial dependent variable specified using
  * ``USFGameInstance::Get()->LogTrialData(DependentVarName, Values)`` or
  * ``USFLoggingBPLibrary::LogTrialData(DependentVariableName, Values)`` (easier to call within a blueprint) 

Also you can use ``USFGameInstance::Get()->LogToHUD(Text)`` to log text into the log pannel of the experimentor view to inform the experimentor about specific things happening or give helpful advices.

# Position Logging with the Study-Framework

## Getting Started

Currently, you can log the position and rotation of actors and components with a specified frequency. For that there are two settings:

- **LogName** is the name that will associated with the log, if left empty, the id name of the actor will be used
- **LogTimer** specifies the logging frequency in Miliseconds. So if set to 20, it will write a log 50 times per second.

The information will be written out as tab-separated values into a file in the `StudyFramework/StudyLogs/PositionLogs/`-directory of your project. **Note:**

- The maximum possible logging frequency is the game's frame rate. So if the frequency of the recorded values is lower than what you set it at, it is probably limited by the frame rate. If you want frame-by-frame position logging, simply set the LogTimer to `0`.
- When an actor/component is added to logging on one map, this will **not** automatically transfer to the other maps. If you want to track a component's / an actor's movements in all maps, you have to add it to logging in each map (see "Tip" below).
- The logging is only active when a condition is active (namely **not** while fading in / fading out), even though the player can still interact with the game during the fading process. The length of the fade can be specified in the StudySetup object settings (see [HowToUse - Further Setup Options](/HowToUse#further-setup-options)).
- You can optionally also log custom data into the position log file, like the status of a character. For that attach a ``USFLogCustomDataComponent`` to the actor/component you want to log and then add this ``USFLogCustomDataComponent`` to the logging instead. This component has a member variable ``FString CustomData`` which you can fill (potentially with more data, then just separate entries in the string by ``"\t"``). It is important that the component is hierachically attached to the root component (potentially with components in between), otherwise the logged position will be zero.
- Remove components if actors/components are destroyed while the map is running, using ``USFLoggingBPLibrary::RemoveComponent``/``USFLoggingBPLibrary::RemoveActor`` or ``Remove Actor/Component from Logging`` in blueprints.

### Example: Logging the Position of the Player in VR

The player position is a bit of a special case, as the movement of the HMD only affects the Head component of the `VirtualRealityPawn` actor that is controlled by the player. So to log the player position we need to add the Head component of the `VirtualRealityPawn` actor to logging. To do that, we first have to open the level/map, in which we want to log the position: `File -> Open Level`. If the `VirtualRealityPawn` actor does not a have a Blueprint associated with it, we have to create one like this:

#### Creating a new Blueprint for an Actor

1. Select the Actor and click on `Blueprint/Add Script` in the `Details` tab\
   ![add-BP-script-1](uploads/fd5933002cbb087c1b82113a37e83f4e/add-BP-script-1.png)
2. We are be prompted with the window seen below. Name and path to where it is saved are not relevant. Example settings are filled in below (I created the folder `Loggables` for the actors I want to log). On a technical level, your actor will be replaced with a copy of your actor (an instance of a new subclass to be precise), that behaves in exactly the same way, with the same settings, but it now additionally has all the features defined in the new Blueprint.\
   ![add-BP-script-2](uploads/66cfa19b7075133104c5c0a8e00a93e4/add-BP-script-2.png)

Now we can edit the Blueprint.

> **Tip:** If we use this actor in multiple levels, we can reuse this loggable version in all of those levels. Simply replace the actor with the new "loggable"-actor. The settings specified in the blueprint will then affect the instances of that actor in all levels. If we want to use different logging settings per actor in different levels, we have to create a new blueprint per level.

#### Using the Blueprint to add VRPawn Head-Component to Logging

- In the `Blueprint Editor` window, open the `Event Graph` ![edit-BP](uploads/a9e257c816ca90aa38d50bd90c585606/edit-BP.png)
- From the `Event BeginPlay` node draw a line from the white arrow to add a new node. Select the `Add Component to Logging` node. ![component-logging1](uploads/fe4afd1be543ffdbea3aed91ef904c87/component-logging1.png)
- Then drag&drop the Head Component into the graph. ![component-logging2](uploads/6b92ee6042f9f859a8c1a1621f3f5cec/component-logging2.png)
- Finally, connect the nodes as seen below. You can adjust the `Log Name` and `Log Timer` within the node. ![component-logging3](uploads/cec65ad399570eba08c87cd9c9086370/component-logging3.png)
- Save and compile the Blueprint when you are done

## Other Position Logging Functionality

- You can **log the position of any component** in the same way as shown above with the VRPawn Head-Component.
- You can also **log the position of actors**:
  - From the `Event BeginPlay` node draw a line from the white arrow to add a new node. Select the `Add Actor to Logging` node. ![addActor-1](uploads/bdd573cb40f6a185b34bc5090e37a719/addActor-1.png)
  - Right-click on the background and place a `Get a reference to self` node ![addActor-2a](uploads/53a2dae9bb04e3aee61d8f3456120a0d/addActor-2a.png)
  - Finally, connect the nodes as seen below. You can adjust the `Log Name` and `Log Timer` within the node. ![addActor-3new](uploads/d63943b03c1a1c1d8084955516e72d7c/addActor-3new.png)
  - Save and compile the Blueprint when you are done
- **Note:** Logging the position of an actor is equivalent to logging the position of their `Root`-component. The `Add Actor to Logging`-function is syntactic sugar.