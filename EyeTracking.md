:warning: **Eye Tracking will only work on Windows right now and only with a Vive Pro Eye** :warning:

# Usage

* In the ``StudySetup`` Actor set ``UseGazeTracker`` to ``EyeTracking`` (if you want to use the actual eye tracker) or ``HeadRotationOnly`` (which just approximates the gaze direction by the head's forward direction; it is the fall-back if no eye tracker is found and ``EyeTracking`` is chosen).
* Object's that should be "gazeable" have to have one of the two components:
  * ``SFGazeTarget``: This has it's own sphere collision which is used for line trace checks (so use this if only part of an actor should be gazeable or even a region greater than the actor itself).
  * ``SFGazeTargetActor``: The whole actor is used for line trace checks.
  * both either use the name specified as ``TargetName`` or if ``USeActorName`` is activated, the name of the actor they are attached to.
* The GazeTracker (e.g. ``USFGameInstance::Get()->GetGazeTracker()``) provides:
  * ``GetCurrentGazeTarget()``: returning the name (``TargetName`` or actor name) of the currently gaze at target or an empty string if nothing "gazeable" is looked at.
  * ``LaunchCalibration()`` to launch a calibration from code.
  * :warning: **NOT IMPLEMENTED YET** :warning: logs the currently gaze at target name and the gaze direction per frame into the participant's log file.

# Prerequisite
 
To add eye tracking you have to add the ``SRanipal`` plugin to your project it can be downloaded as part of the SDK [here](https://developer-express.vive.com/resources/vive-sense/eye-and-facial-tracking-sdk/download/latest/) (HTC Vive account required)\
:warning: Make sure that the ``Plugins/SRanipal/Binaries`` folder is commited to your project. In case it is ignored by default do ``git add -f Plugins/SRanipal/Binaries``

Also in your project you have to have the ``SRanpial`` plugin activated in the .uproject file
```
"Plugins": [
		{
			"Name": "SRanipal",
			"Enabled": true
		}
	],
```

# Starting

For any HTC Vive Pro Eye eye tracking to work:
* Steam (VR) for me needed to be started as admin
* SR_Runtime needs to be started (as admin)
* For development potentially also Visual Studio starting Unreal need to be run as admin

If this is not done, eye calibration is not started correctly.

Some more insights can be found at: [Unreal Eye Tracking Demo Project](https://devhub.vr.rwth-aachen.de/VR-Group/unreal-eye-tracking/-/wikis/home)