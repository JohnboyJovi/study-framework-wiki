Here some examples of randomized conditions and the ideas behind those can be found. **For simplicity, I left out ``USFMapFactors`` in all of them, which are however obviously required, just imagine all of the phases run on the same map.**
I also provide ``StudySetup.json`` declarations (which are by default collapsed for better readability) and can be used for testing, e.g., in the [Study Framework Demo project](https://git-ce.rwth-aachen.de/vr-vis/VR-Group/unreal-development/demos/study-framework-demo).

# Fully ``Random``
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
| 6 | 🟠1 | 🟠2 | 🟢2 | 🔵1 | 🟢1 | 🔵2 |
| ... |

Notice that after 6 runs orders will be repeated, so having a multiple of 6 participants would be recommended here. *Also note that you can nicely see the ``Balanced Latin Square`` structure here, having in each column and row each condition exactly once and having each condition being followed by every other condition exactly once!*

# Using ``EnBlock``
If you want to have, e.g., always the same colored repetition next to each other, you can you ``EnBlock``

* Color: {🟠, 🔵, 🟢} (``Mixing Order: EnBlock``)
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
					"MixingOrder": "EnBlock",
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
</details>
</p>

| participant # |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠1 | 🟠2 | 🔵2 | 🔵1 | 🟢1 | 🟢2 |
| 1 | 🟠2 | 🟠1 | 🟢1 | 🟢2 | 🔵2 | 🔵1 |
| 2 | 🟢1 | 🟢2 | 🟠2 | 🟠1 | 🔵1 | 🔵2 |
| 3 | 🟢2 | 🟢1 | 🔵1 | 🔵2 | 🟠2 | 🟠1 |
| 4 | 🔵1 | 🔵2 | 🟢2 | 🟢1 | 🟠1 | 🟠2 |
| 5 | 🔵2 | 🔵1 | 🟠1 | 🟠2 | 🟢2 | 🟢1 |
| ... |



# Using ``InOrder`` (potentially for multiple factors)
``InOrder``

* Color: {🟠, 🔵, 🟢} (``Mixing Order: InOrder``)
* Number: {1, 2} (``Mixing Order: InOrder``)
* Letter: {a, b, c} (``Mixing Order: Random``)

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
					"MixingOrder": "InOrder",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Number",
					"Levels": [
						"1",
						"2"
					],
					"MixingOrder": "InOrder",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Letter",
					"Levels": [
						"a",
						"b",
						"c"
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
</details>
</p>

| participant # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 a | 🟠 1 b | 🟠 1 c | 🟠 2 a | 🟠 2 c | 🟠 2 b | 🔵 1 c | 🔵 1 a | 🔵 1 b | 🔵 2 c | 🔵 2 b | 🔵 2 a | 🟢 1 b | 🟢 1 c | 🟢 1 a | 🟢 2 b | 🟢 2 a | 🟢 2 c |
| 1 | 🟠 1 a | 🟠 1 c | 🟠 1 b | 🟠 2 c | 🟠 2 a | 🟠 2 b | 🔵 1 c | 🔵 1 b | 🔵 1 a | 🔵 2 b | 🔵 2 c | 🔵 2 a | 🟢 1 b | 🟢 1 a | 🟢 1 c | 🟢 2 a | 🟢 2 b | 🟢 2 c |
| 2 | 🟠 1 c | 🟠 1 a | 🟠 1 b | 🟠 2 c | 🟠 2 b | 🟠 2 a | 🔵 1 b | 🔵 1 c | 🔵 1 a | 🔵 2 b | 🔵 2 a | 🔵 2 c | 🟢 1 a | 🟢 1 b | 🟢 1 c | 🟢 2 a | 🟢 2 c | 🟢 2 b |
| 3 | 🟠 1 c | 🟠 1 b | 🟠 1 a | 🟠 2 b | 🟠 2 c | 🟠 2 a | 🔵 1 b | 🔵 1 a | 🔵 1 c | 🔵 2 a | 🔵 2 b | 🔵 2 c | 🟢 1 a | 🟢 1 c | 🟢 1 b | 🟢 2 c | 🟢 2 a | 🟢 2 b |
| 4 | 🟠 1 b | 🟠 1 c | 🟠 1 a | 🟠 2 b | 🟠 2 a | 🟠 2 c | 🔵 1 a | 🔵 1 b | 🔵 1 c | 🔵 2 a | 🔵 2 c | 🔵 2 b | 🟢 1 c | 🟢 1 a | 🟢 1 b | 🟢 2 c | 🟢 2 b | 🟢 2 a |
| 5 | 🟠 1 b | 🟠 1 a | 🟠 1 c | 🟠 2 a | 🟠 2 b | 🟠 2 c | 🔵 1 a | 🔵 1 c | 🔵 1 b | 🔵 2 c | 🔵 2 a | 🔵 2 b | 🟢 1 c | 🟢 1 b | 🟢 1 a | 🟢 2 b | 🟢 2 c | 🟢 2 a |
| 6 | 🟠 1 a | 🟠 1 b | 🟠 1 c | 🟠 2 a | 🟠 2 c | 🟠 2 b | 🔵 1 c | 🔵 1 a | 🔵 1 b | 🔵 2 c | 🔵 2 b | 🔵 2 a | 🟢 1 b | 🟢 1 c | 🟢 1 a | 🟢 2 b | 🟢 2 a | 🟢 2 c |
| ... |

Notice that the first ``inOrder`` factor ``Color`` is kept in order for all participants. ``Number``, however, while being kept in order for each level of ``Color``, jumps back and forth over the entire run.



# Combining ``EnBlock``, ``InOrder`` and ``Random``
If you want to have, e.g., always the same colored repetition next to each other, you can you ``EnBlock``

* Color: {🟠, 🔵, 🟢} (``Mixing Order: EnBlock``)
* Number: {1, 2} (``Mixing Order: InOrder``)
* Letter: {a, b} (``Mixing Order: Random``)

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
					"MixingOrder": "EnBlock",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "letter",
					"Levels": [
						"a",
						"b"
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
					"MixingOrder": "InOrder",
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
</details>
</p>

| participant # |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 a | 🟠 1 b | 🟠 2 b | 🟠 2 a | 🔵 1 b | 🔵 1 a | 🔵 2 a | 🔵 2 b | 🟢 1 a | 🟢 1 b | 🟢 2 b | 🟢 2 a |
| 1 | 🟠 1 b | 🟠 1 a | 🟠 2 a | 🟠 2 b | 🟢 1 a | 🟢 1 b | 🟢 2 b | 🟢 2 a | 🔵 1 b | 🔵 1 a | 🔵 2 a | 🔵 2 b |
| 2 | 🟢 1 a | 🟢 1 b | 🟢 2 b | 🟢 2 a | 🟠 1 b | 🟠 1 a | 🟠 2 a | 🟠 2 b | 🔵 1 a | 🔵 1 b | 🔵 2 b | 🔵 2 a |
| 3 | 🟢 1 b | 🟢 1 a | 🟢 2 a | 🟢 2 b | 🔵 1 a | 🔵 1 b | 🔵 2 b | 🔵 2 a | 🟠 1 b | 🟠 1 a | 🟠 2 a | 🟠 2 b |
| 4 | 🔵 1 a | 🔵 1 b | 🔵 2 b | 🔵 2 a | 🟢 1 b | 🟢 1 a | 🟢 2 a | 🟢 2 b | 🟠 1 a | 🟠 1 b | 🟠 2 b | 🟠 2 a |
| 5 | 🔵 1 b | 🔵 1 a | 🔵 2 a | 🔵 2 b | 🟠 1 a | 🟠 1 b | 🟠 2 b | 🟠 2 a | 🟢 1 b | 🟢 1 a | 🟢 2 a | 🟢 2 b |
| 6 | 🟠 1 a | 🟠 1 b | 🟠 2 b | 🟠 2 a | 🔵 1 b | 🔵 1 a | 🔵 2 a | 🔵 2 b | 🟢 1 a | 🟢 1 b | 🟢 2 b | 🟢 2 a |
| ... |

# ``NonCombined``: Adding randomness without creating aditional conditions
If the letter in the above example should simply add some randomness ut not increase the combinatorical blowup, ``NonCombined`` can be used. This means that all combination of ``Color`` and ``Number`` are produced, but not all combinations ``Letter`` with those.

* Color: {🟠, 🔵, 🟢} (``Mixing Order: EnBlock``)
* Number: {1, 2} (``Mixing Order: InOrder``)
* Letter: {a, b} (``Mixing Order: Random``, ``NonCombined: true``)

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
					"MixingOrder": "EnBlock",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "letter",
					"Levels": [
						"a",
						"b"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": true
				},
				{
					"FactorName": "Number",
					"Levels": [
						"1",
						"2"
					],
					"MixingOrder": "InOrder",
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
</details>
</p>

| participant # |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 a | 🟠 2 b | 🔵 1 a | 🔵 2 b | 🟢 1 a | 🟢 2 b |
| 1 | 🟠 1 b | 🟠 2 a | 🟢 1 b | 🟢 2 a | 🔵 1 b | 🔵 2 a |
| 2 | 🟢 1 a | 🟢 2 b | 🟠 1 a | 🟠 2 b | 🔵 1 a | 🔵 2 b |
| 3 | 🟢 1 b | 🟢 2 a | 🔵 1 b | 🔵 2 a | 🟠 1 b | 🟠 2 a |
| 4 | 🔵 1 a | 🔵 2 b | 🟢 1 a | 🟢 2 b | 🟠 1 a | 🟠 2 b |
| 5 | 🔵 1 b | 🔵 2 a | 🟠 1 b | 🟠 2 a | 🟢 1 b | 🟢 2 a |
| 6 | 🟠 1 a | 🟠 2 b | 🔵 1 a | 🔵 2 b | 🟢 1 a | 🟢 2 b |
| ... |


Note that we only have 6 conditions here per run, instead of the 12 we had in the example above where ``NonCombied`` was not used.

# ``Between``-subject factors
So far all examples only used ``Within``-subject factors, where each participant should see all levels. However, ``Type`` can also be set to ``Between`` such that every participant only sees exactly one level of this factor.

* Color: {🟠, 🔵, 🟢} (``Mixing Order: RandomOrder``, ``Type: Within``)
* Number: {1, 2} (``Mixing Order: RandomOrder``, ``Type: Between``)

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
					"Type": "Between",
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
</details>
</p>

| participant # |  |  |  |
| --- | --- | --- | --- |
| 0 | 🟠 1 | 🔵 1 | 🟢 1 |
| 1 | 🟠 2 | 🟢 2 | 🔵 2 |
| 2 | 🟢 1 | 🟠 1 | 🔵 1 |
| 3 | 🟢 2 | 🔵 2 | 🟠 2 |
| 4 | 🔵 1 | 🟢 1 | 🟠 1 |
| 5 | 🔵 2 | 🟠 2 | 🟢 2 |
| 6 | 🟠 1 | 🔵 1 | 🟢 1 |
| ... |

Notice that every participants either only sees ``1``s or ``2``s.

# Repetition defined per Phase

The following three examples all use the same factors:

* Color: {🟠, 🔵} (``Mixing Order: RandomOrder``)
* Number: {1, 2} (``Mixing Order: RandomOrder``)
* ``Number Of Repetitions: 2``

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
						"Blue"
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
			"Number Of Repetitions": 2,
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
</details>
</p>

## ``Type of Repetition: SameOrder``

| participant # |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 |
| 1 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 |
| 2 | 🔵 1 | 🔵 2 | 🟠 2 | 🟠 1 | 🔵 1 | 🔵 2 | 🟠 2 | 🟠 1 |
| 3 | 🔵 2 | 🟠 1 | 🔵 1 | 🟠 2 | 🔵 2 | 🟠 1 | 🔵 1 | 🟠 2 |
| 4 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 |
| ... |

The second four conditions are exactly in the same order as the first four.

## ``Type of Repetition: SameOrder``

| participant # |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 |
| 1 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 | 🔵 1 | 🔵 2 | 🟠 2 | 🟠 1 |
| 2 | 🔵 1 | 🔵 2 | 🟠 2 | 🟠 1 | 🔵 2 | 🟠 1 | 🔵 1 | 🟠 2 |
| 3 | 🔵 2 | 🟠 1 | 🔵 1 | 🟠 2 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 |
| 4 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 |
| ... |

Note that all conditions are seen exactly once before they are repeated a second time.

## ``Type of Repetition: Fully Random``

| participant # |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 1 | 🟠 1 | 🔵 2 | 🟠 2 | 🔵 2 | 🟠 2 | 🔵 1 | 🔵 1 |
| 1 | 🟠 1 | 🟠 2 | 🟠 1 | 🟠 2 | 🔵 2 | 🔵 1 | 🔵 2 | 🔵 1 |
| 2 | 🟠 2 | 🟠 2 | 🟠 1 | 🔵 1 | 🟠 1 | 🔵 1 | 🔵 2 | 🔵 2 |
| 3 | 🟠 2 | 🔵 1 | 🟠 2 | 🔵 1 | 🟠 1 | 🔵 2 | 🟠 1 | 🔵 2 |
| 4 | 🔵 1 | 🔵 1 | 🟠 2 | 🔵 2 | 🟠 2 | 🔵 2 | 🟠 1 | 🟠 1 |
| 5 | 🔵 1 | 🔵 2 | 🔵 1 | 🔵 2 | 🟠 2 | 🟠 1 | 🟠 2 | 🟠 1 |
| 6 | 🔵 2 | 🔵 2 | 🔵 1 | 🟠 1 | 🔵 1 | 🟠 1 | 🟠 2 | 🟠 2 |
| 7 | 🔵 2 | 🟠 1 | 🔵 2 | 🟠 1 | 🔵 1 | 🟠 2 | 🔵 1 | 🟠 2 |
| 8 ... |

Note that this requires not a multiple of 4 but of 8 participants to be perfectly counterbalanced. Also when randomizig it it not considered that 🟠 1 = 🟠 1 they are treated as two separate conditions in the Latin Square, which can yield some patterns reoccuring more often then others. However, it is hard to tell what a better solution would be.







---
Here is the python script used to automatically generate those tables. In case new examples should be added:
<p>
<details>
<summary>WikiTableGenerator.py</summary>

```
orange = "🟠" #not shown correctly here but show correctly in gitlab Wiki
green = "🟢"
blue = "🔵"


def WriteHeader(numberCells):
  outputlines = []
  output = "| participant # |"
  for i in range(numberCells):
    output += "  |"
  outputlines.append(output)

  output = "|"
  for i in range(numberCells+1):
    output += " --- |"
  outputlines.append(output)
  return outputlines

with open('GeneratedDebugRuns.txt') as f:
    lines = f.readlines()

    outputlines = []

    for line in lines:
      entries = line.split("\t")
      if len(outputlines) == 0:
        outputlines = WriteHeader(len(entries)-1)
      outLine = "| "+str(entries[0])+" |"
      for i in range(1, len(entries)):
        condition = entries[i]
        
        #color
        if "Green" in condition:
          outLine += " " + green
        elif "Orange" in condition:
          outLine += " " + orange
        elif "Blue" in condition:
          outLine += " " + blue

        #number
        if "_1" in condition:
          outLine += " 1"
        elif "_2" in condition:
          outLine += " 2"

        #letter
        if "_a" in condition:
          outLine += " a"
        elif "_b" in condition:
          outLine += " b"
        elif "_c" in condition:
          outLine += " c"

        outLine += " |"
      outputlines.append(outLine)

    print(outputlines)
    outFile = open('table.txt', 'w', encoding="utf-8")
    for outline in outputlines:    
      outFile.write(outline+"\n")
    outFile.close()

              

```
</details>
</p>