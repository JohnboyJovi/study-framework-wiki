# Prerequisite
To add eye tracking you have to add the ``SRanipal`` plugin to your project it can be downloaded as part of the SDK [here](https://developer-express.vive.com/resources/vive-sense/eye-and-facial-tracking-sdk/download/latest/) (HTC Vive account required)

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

As of now you need Admin rights to use eye tracking. Both ``SRanipalRuntime`` and ``Unreal`` have to be started with admin rights (if you use ``Visual Studio`` to start Unreal, just start Visual Studio with admin rights).