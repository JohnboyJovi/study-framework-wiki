Here are some examples of randomized conditions and the ideas behind those can be found. **For simplicity, I left out ``USFMapFactors`` in all of them, which are however obviously required, just imagine all of the phases run on the same map.**
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
			]
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
			]
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
			]
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
			]
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
			]
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
			]
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



# Repeating all conditions multiple times

This can be done by adding an additional repetition factor that either **makes sure that first all conditions are seen before they are repeated (and the same for the third etc. repetition)**

* Color: {🟠, 🔵} (``Mixing Order: RandomOrder``)
* Letter: {a, b} (``Mixing Order: RandomOrder``)
* Repetition: {1, 2} (``Mixing Order: InOrder``)

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
					"FactorName": "Letter",
					"Levels": [
						"a",
						"b"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Repetition",
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
			]
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

| participant # |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 a 1 | 🟠 b 1 | 🔵 b 1 | 🔵 a 1 | 🟠 b 2 | 🔵 a 2 | 🟠 a 2 | 🔵 b 2 |
| 1 | 🟠 b 1 | 🔵 a 1 | 🟠 a 1 | 🔵 b 1 | 🔵 a 2 | 🔵 b 2 | 🟠 b 2 | 🟠 a 2 |
| 2 | 🔵 a 1 | 🔵 b 1 | 🟠 b 1 | 🟠 a 1 | 🔵 b 2 | 🟠 a 2 | 🔵 a 2 | 🟠 b 2 |
| 3 | 🔵 b 1 | 🟠 a 1 | 🔵 a 1 | 🟠 b 1 | 🟠 a 2 | 🟠 b 2 | 🔵 b 2 | 🔵 a 2 |
| 4 | 🟠 a 1 | 🟠 b 1 | 🔵 b 1 | 🔵 a 1 | 🟠 b 2 | 🔵 a 2 | 🟠 a 2 | 🔵 b 2 |
| ... |

But repetition can, e.g., also be configured to always **show all 🟠 conditions and their repetitions together**

* Color: {🟠, 🔵} (``Mixing Order: EnBlock``)
* Letter: {a, b} (``Mixing Order: RandomOrder``)
* Repetition: {1, 2} (``Mixing Order: InOrder``)

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
					"MixingOrder": "EnBlock",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Letter",
					"Levels": [
						"a",
						"b"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false
				},
				{
					"FactorName": "Repetition",
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
			]
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

| participant # |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 🟠 a 1 | 🟠 b 1 | 🟠 b 2 | 🟠 a 2 | 🔵 b 1 | 🔵 a 1 | 🔵 a 2 | 🔵 b 2 |
| 1 | 🔵 b 1 | 🔵 a 1 | 🔵 a 2 | 🔵 b 2 | 🟠 a 1 | 🟠 b 1 | 🟠 b 2 | 🟠 a 2 |
| 2 | 🟠 a 1 | 🟠 b 1 | 🟠 b 2 | 🟠 a 2 | 🔵 b 1 | 🔵 a 1 | 🔵 a 2 | 🔵 b 2 |
| ... |

Note that in this case there is more regularity then we would like to have due to the layout and usage of the Latin Square table. If this is a problem, you have to use the ``ConditionSortingCallback()`` function (see below).

# Phase Randomization

In this example we have split our task in two phases with a break in between:

* Phase 1
  * Color: {🟠, 🟢} (``Mixing Order: RandomOrder``)
  * Letter: {a, b} (``Mixing Order: RandomOrder``)
  * Number: {1, 2, 3, 4, 5, 6, 7, 8} (``NonCombined: true``) This could, e.g., be different task participants have to do
* Break
* Phase 2 (set in italic)
  * Color: {🔵} (``Mixing Order: RandomOrder``)
  * Letter: {a, b} (``Mixing Order: RandomOrder``)
  * Number: {1, 2, 3, 4, 5, 6, 7, 8} (``NonCombined: true``) This could, e.g., be different task participants have to do

<p>
<details>
<summary>StudySetup.json</summary>

```
{
	"Phases": [
		{
			"Name": "Phase1",
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
						"Green"
					],
					"MixingOrder": "RandomOrder",
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
					"FactorName": "number",
					"Levels": [
						"1",
						"2",
						"3",
						"4",
						"5",
						"6",
						"7",
						"8"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": true
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
			]
		},
		{
			"Name": "Break",
			"Factors": [
				{
					"FactorName": "Map",
					"Levels": [
						"BreakMap"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false,
					"MapFactor": true
				}
			],
			"Dependent Variables": []
		},
		{
			"Name": "Phase2",
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
						"Blue"
					],
					"MixingOrder": "RandomOrder",
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
					"FactorName": "number",
					"Levels": [
						"1",
						"2",
						"3",
						"4",
						"5",
						"6",
						"7",
						"8"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": true
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
			]
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

| participant # |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |🟠 a 1 |🟠 b 2 |🟢 b 8 |🟢 a 3 |Break |*🔵 a 3* |*🔵 b 4* |
| 1 |🟠 b 2 |🟢 a 3 |🟠 a 1 |🟢 b 4 |Break |*🔵 b 4* |*🔵 a 5* |
| 2 |🟢 a 3 |🟢 b 4 |🟠 b 2 |🟠 a 5 |Break |*🔵 a 5* |*🔵 b 6* |
| 3 |🟢 b 4 |🟠 a 5 |🟢 a 3 |🟠 b 6 |Break |*🔵 b 6* |*🔵 a 7* |
| 4 |🟠 a 5 |🟠 b 6 |🟢 b 4 |🟢 a 7 |Break |*🔵 a 7* |*🔵 b 8* |
| 5 |🟠 b 6 |🟢 a 7 |🟠 a 5 |🟢 b 8 |Break |*🔵 b 8* |*🔵 a 1* |
| 6 |🟢 a 7 |🟢 b 8 |🟠 b 6 |🟠 a 1 |Break |*🔵 a 1* |*🔵 b 2* |
| 7 |🟢 b 8 |🟠 a 1 |🟢 a 7 |🟠 b 2 |Break |*🔵 b 2* |*🔵 a 3* |
| 8 |🟠 a 1 |🟠 b 2 |🟢 b 8 |🟢 a 3 |Break |*🔵 a 3* |*🔵 b 4* |
| ... |

Here we can now keep everything the same and just specify ``Phases To Order Randomize: {Phase 1, Phase 2}``, which yields:

| participant # |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |🟠 a 1 |🟠 b 2 |🟢 b 8 |🟢 a 3 |Break |*🔵 a 3* |*🔵 b 4* |
| 1 |*🔵 b 4* |*🔵 a 5* |Break |🟠 b 2 |🟢 a 3 |🟠 a 1 |🟢 b 4 |
| 2 |🟢 a 3 |🟢 b 4 |🟠 b 2 |🟠 a 5 |Break |*🔵 a 5* |*🔵 b 6* |
| 3 |*🔵 b 6* |*🔵 a 7* |Break |🟢 b 4 |🟠 a 5 |🟢 a 3 |🟠 b 6 |
| 4 |🟠 a 5 |🟠 b 6 |🟢 b 4 |🟢 a 7 |Break |*🔵 a 7* |*🔵 b 8* |
| 5 |*🔵 b 8* |*🔵 a 1* |Break |🟠 b 6 |🟢 a 7 |🟠 a 5 |🟢 b 8 |
| 6 |🟢 a 7 |🟢 b 8 |🟠 b 6 |🟠 a 1 |Break |*🔵 a 1* |*🔵 b 2* |
| 7 |*🔵 b 2* |*🔵 a 3* |Break |🟢 b 8 |🟠 a 1 |🟢 a 7 |🟠 b 2 |
| 8 |🟠 a 1 |🟠 b 2 |🟢 b 8 |🟢 a 3 |Break |*🔵 a 3* |*🔵 b 4* |
| ... |

What is still suboptimal is that the ``nonCombined`` factor (Number) is not coordinated between the phases. If we think of it as some task the participants have to do, that we would want participants to only see each number at most once (in both phases together) but this cannot be coordinated between two phases as of now. See, for example, participant # 1, who sees number 4 two times but never, e.g., 2.
This problem is tackled in the next section, by using the **``ConditionSortingCallback()``** function.

# ``ConditionSortingCallback()`` to manually sort everything as needed

You first have to create a c++ class derived from ``ASFStudySetup``, which implements a single method ``virtual TArray<USFCondition*> ConditionSortingCallback(const TArray<USFCondition*>& Conditions);``

We use a similar setup as above:

* Phase 1
  * Color: {🟠, 🟢, 🔵} (``Mixing Order: EnBlock``)
  * Letter: {a, b} (``Mixing Order: RandomOrder``)
  * Number: {1, 2, 3, 4, 5, 6, 7, 8} (``NonCombined: true``) This could, e.g., be different task participants have to do
* Break

<p>
<details>
<summary>StudySetup.json</summary>

```
{
	"Phases": [
		{
			"Name": "Phase1",
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
						"Green",
						"Blue"
					],
					"MixingOrder": "RandomOrder",
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
					"FactorName": "number",
					"Levels": [
						"1",
						"2",
						"3",
						"4",
						"5",
						"6",
						"7",
						"8"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": true
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
			]
		},
		{
			"Name": "Break",
			"Factors": [
				{
					"FactorName": "Map",
					"Levels": [
						"BreakMap"
					],
					"MixingOrder": "RandomOrder",
					"Type": "Within",
					"NonCombined": false,
					"MapFactor": true
				}
			],
			"Dependent Variables": []
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

Additionally we implement the callback function

```c++
TArray<USFCondition*> AStudySetup::ConditionSortingCallback(const TArray<USFCondition*>& Conditions, int ParticipantRunningNumber) const
{
	TArray<USFCondition*> ReorderedConditions;
	for(USFCondition* Condition : Conditions)
	{
		if(Condition->PhaseName == "Break")
		{
			ReorderedConditions.Insert(Condition, 4);
		}
		else
		{
			ReorderedConditions.Add(Condition);
		}
	}
	return ReorderedConditions;
}
```

| participant # |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |🟠 a 1 |🟠 b 2 |🟢 b 8 |🟢 a 3 |Break |🔵 a 7 |🔵 b 4 |
| 1 |🟠 b 2 |🟠 a 3 |🔵 a 1 |🔵 b 4 |Break |🟢 b 8 |🟢 a 5 |
| 2 |🔵 a 3 |🔵 b 4 |🟠 b 2 |🟠 a 5 |Break |🟢 a 1 |🟢 b 6 |
| 3 |🔵 b 4 |🔵 a 5 |🟢 a 3 |🟢 b 6 |Break |🟠 b 2 |🟠 a 7 |
| 4 |🟢 a 5 |🟢 b 6 |🔵 b 4 |🔵 a 7 |Break |🟠 a 3 |🟠 b 8 |
| 5 |🟢 b 6 |🟢 a 7 |🟠 a 5 |🟠 b 8 |Break |🔵 b 4 |🔵 a 1 |
| 6 |🟠 a 7 |🟠 b 8 |🟢 b 6 |🟢 a 1 |Break |🔵 a 5 |🔵 b 2 |
| 7 |🟠 b 8 |🟠 a 1 |🔵 a 7 |🔵 b 2 |Break |🟢 b 6 |🟢 a 3 |
| 8 |🔵 a 1 |🔵 b 2 |🟠 b 8 |🟠 a 3 |Break |🟢 a 7 |🟢 b 4 |
| 9 |🔵 b 2 |🔵 a 3 |🟢 a 1 |🟢 b 4 |Break |🟠 b 8 |🟠 a 5 |
| 10 |🟢 a 3 |🟢 b 4 |🔵 b 2 |🔵 a 5 |Break |🟠 a 1 |🟠 b 6 |
| 11 |🟢 b 4 |🟢 a 5 |🟠 a 3 |🟠 b 6 |Break |🔵 b 2 |🔵 a 7 |

So here we moved the break phase to the point where two colors are done. 
This callback function obviously also yields a lot more possibilities, just make sure that you take care for the counterbalancing when extensively using it.

# ``ConditionSortingCallback()`` to manually shuffle all conditions in a phase randomly

Sometimes the given randomization might not be enough, e.g., when you have a lot of conditions (e.g., 8x8 comparison tasks). Then you might want to simply shuffle all conditions in a phase randomly for each participants to avoid having emerging order patterns per participant.

A possible code soulution in the ``ConditionSortingCallback()`` function could be:

```c++
TArray<USFCondition*> AStudySetup::ConditionSortingCallback(const TArray<USFCondition*>& Conditions, int ParticipantRunningNumber) const
{
	//first split the coditions:
	TArray<USFCondition*> ConditionsBefore;
	TArray<USFCondition*> ConditionsToShuffle;
	TArray<USFCondition*> ConditionsAfter;
	bool bFoundFirst = false;
	for(USFCondition* Condition : Conditions)
	{
		if(Condition->PhaseName == "Decision")
		{
			bFoundFirst = true;
			ConditionsToShuffle.Add(Condition);
		}
		else
		{
			if(!bFoundFirst)
			{
				ConditionsBefore.Add(Condition);
			}
			else
			{
				ConditionsAfter.Add(Condition);
			}
		}
	}

	//now shuffle the conditions:
	TArray<USFCondition*> ShuffledConditions;
	//seed a random number generator with the participant's running number, so shuffling is predictable
	FRandomStream RNG(ParticipantRunningNumber);
	while(ConditionsToShuffle.Num() > 0) //while there are still unshuffled conditions
	{
		int PickIndex = RNG.RandRange(0, ConditionsToShuffle.Num() - 1);
		ShuffledConditions.Add(ConditionsToShuffle[PickIndex]);
		ConditionsToShuffle.RemoveAt(PickIndex);
	}

	//put everything back together
	TArray<USFCondition*> ReorderedConditions = ConditionsBefore;
	ReorderedConditions.Append(ShuffledConditions)
	ReorderedConditions.Append(ConditionsAfter)

	return ReorderedConditions;
}
```

---
---
Here is the python script used to automatically generate those tables. In case new examples should be added:
<p>
<details>
<summary>WikiTableGenerator.py</summary>

```
orange = "🟠" #not shown correctly in IDLE but shown correctly in gitlab Wiki
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

        entryString = ""
        #color
        if "Green" in condition:
          entryString += green
        elif "Orange" in condition:
          entryString += orange
        elif "Blue" in condition:
          entryString += blue

        #letter
        if "_a" in condition:
          entryString += " a"
        elif "_b" in condition:
          entryString += " b"
        elif "_c" in condition:
          entryString += " c"

        #number
        for i in range(1,9):
          if "_"+str(i) in condition:
            entryString += " " + str(i)

        #phases
        if "Phase2" in condition:
          #make it italic
          entryString = "*" + entryString + "*"
        elif "Break" in condition:
          entryString = "Break"
    

        outLine += entryString + " |"
      outputlines.append(outLine)

    print(outputlines)
    outFile = open('table.txt', 'w', encoding="utf-8")
    for outline in outputlines:    
      outFile.write(outline+"\n")
    outFile.close()
              
```
</details>
</p>