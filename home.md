**User Studies:**
User studies are a non-trivial, but essential part of our research. After you carefully structured and designed your study (e.g., user task, a decision between within- and between-subjects design, number of conditions, etc.), the framework provided here shall help you with setting up the study code-wise. In addition to this, you require various questionnaires to get more insights into the participant's thoughts and preferences. Information on those questionnaires as well as the procedure of a study can be found [in this separate subsection](StudyProcedure).

**Goals of the StudyFramework are:**
* Make it easy to setup/prototype studies in UE
* Produce data that is easy to analyze
* Have similar data for different studies (facilitating meta-analyses and sharing analysis tools)
* Do **not** overengineer

For information on how to use this, go to:

The [HowToUse-Section](HowToUse)

Additional information:
- [What is logged and where?](Logging)
- [What are all these classes?](Architecture)
- [How can I use eye tracking](EyeTracking)
- [Some possible solutions to problems can be found in the Trouble Shooting Section](Trouble-Shooting)

**Features provided by the framework are:**
* Quickly set up a study with a factorial design
* Fading between levels/conditions
* HUD for easier controlling of the study
* store data in format ready-to-use in statistics software
* Write out run data and last participant in json
* Start a map and be able to debug it directly
* Run on different systems: desktop, HMD, CAVE (nDisplay not tested yet!)
* Being able to recover from crashes (continue the study in the condition that was not finished)
