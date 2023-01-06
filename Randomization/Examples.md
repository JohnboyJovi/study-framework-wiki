Here some examples of randomized conditions and the ideas behind those can be found. **For simplicity, I left out ``USFMapFactors`` in all of them, which are however obviously required, just imagine all of the phases run on the same map.**
I also provide ``StudySetup.json`` declarations (which are by default collapsed for better readability) and can be used for testing, e.g., in the [Study Framework Demo project](https://git-ce.rwth-aachen.de/vr-vis/VR-Group/unreal-development/demos/study-framework-demo).

# Fully Random
If you have two factors and want to fully randomize the order of presentation of their combinations for different participants. <br>
* Color: {🟠, 🔵, 🟢} (``Mixing Order: Random``)
* Number: {1, 2} (``Mixing Order: Random``)

<p>
<details>
<summary>StudySetup.json</summary>

```
{
	"Phases": [
		{
			"Name": "Study",
			"Factors": [
				{
					"FactorName": "Map",
					"Levels": [
						"/Game/Maps/StudyMap1"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false,
					"MapFactor": true
				},
				{
					"FactorName": "TextColor",
					"Levels": [
						"Orange",
						"Blue",
						"Green"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Number",
					"Levels": [
						"1",
						"2"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false
				}
			],
			"Dependent Variables": [
				{
					"Name": "Visibility",
					"Required": true
				},
				{
					"Name": "OtherData",
					"Required": false
				}
			],
			"Number Of Repetitions": 1,
			"TypeOfRepetition": "SameOrder"
		}
	],
	"PhasesToOrderRandomize": [],
	"FadeConfig":
	{
		"StartFadedOut": true,
		"FadeDuration": 2,
		"FadeOutDuration": 1,
		"FadeColor": "(R=0.000000,G=0.000000,B=0.000000,A=1.000000)"
	},
	"ExperimenterViewConfig":
	{
		"ShowHUD": true,
		"ShowConditionsPanelByDefault": false,
		"ShowExperimenterViewInSecondWindow": false,
		"SecondWindowSizeX": 1920,
		"SecondWindowSizeY": 1080,
		"SecondWindowPosX": 1920,
		"SecondWindowPosY": 0
	},
	"UseGazeTracker": "NotTracking"
}
```
<pre><code>PASTE LOGS HERE</code></pre>

</details>
</p>


| participant # |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠1 | 🟠2 | 🟢2 | 🔵1 | 🟢1 | 🔵2 |
| 1 | 🟠2 | 🔵1 | 🟠1 | 🔵2 | 🟢2 | 🟢1 |
| 2 | 🔵1 | 🔵2 | 🟠2 | 🟢1 | 🟠1 | 🟢2 |
| 3 | 🔵2 | 🟢1 | 🔵1 | 🟢2 | 🟠2 | 🟠1 |
| 4 | 🟢1 | 🟢2 | 🔵2 | 🟠1 | 🔵1 | 🟠2 |
| 5 | 🟢2 | 🟠1 | 🟢1 | 🟠2 | 🔵2 | 🔵1 |

After that orders will be repeated, so having a multiple of 6 participants would be recommended here. *Also note that you can nicely see the ``Balanced Latin Square`` structure here, having in each column and row each condition exactly once and having each condition being followed by every other condition exactly once!*