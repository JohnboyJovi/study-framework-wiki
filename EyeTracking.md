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