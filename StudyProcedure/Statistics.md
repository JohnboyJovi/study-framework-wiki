Here are some hints and ideas how to evaluate the gathered data.

# Software

One possibility is to use RStudio. (Install r: https://cran.rstudio.com/, and then install RStudio: https://posit.co/download/rstudio-desktop/)

All of the scripts below are for RStudio, but for example also *jamovi* (https://www.jamovi.org/) can be used (which provides most functionality for statistic tests in a simple GUI, but is not so versatile for plotting).

# Demographics

If you gathered demogrpahic data, e.g., with SoSciSurvey, you should report who participated, by giving their number ``n=...`` participants, their gender count and at least age with mean (M) and standard deviation (SD).

``SoSciSurvey data`` ca be easily loaded into RStudio with the script provided alongside the data on ScoSciSurvey.

*For all the following examples you abviously have to adapt the names of the data frames (here, e.g., soscisurveyData and columns, here, e.g., D001)*

<details><summary>This is a script for counting occurences</summary>

```r
add_descriptive_statistics <- function(data, name){
  print(name)
  print(table(data))
}

#can be used, e.g., for:
add_descriptive_statistics(soscisurveyData$D001, "Gender")
add_descriptive_statistics(soscisurveyData$D004, "VR Frequency")


```

</details>

<details><summary>Here is a script for quantitative statistics</summary>

```r
add_qualitative_statistics <- function(data, name, demographics_stats){
  old_names = rownames(demographics_stats)
  demographics_stats= rbind(demographics_stats, data.frame("Mean"=mean(data), 
                                                           "SD"=sd(data), 
                                                           "Min"=min(data), 
                                                           "Max"=max(data)))
  rownames(demographics_stats) = append(old_names, name)
  demographics_stats
}


#and applied to age data from a SoSciSurvey data frame
soscisurveyData$D002_01 <- as.numeric(soscisurveyData$D002_01)
demographics_stats = data.frame()
demographics_stats = add_qualitative_statistics(soscisurveyData$D002_01, "Age",demographics_stats)


```

</details>

# Data Preparation

The data gathered by the study framework should already be in an easily digestable format and can be loaded by:
```
ActData <- read.csv(file = 'Phase_Act.csv')
```

<details><summary>If you want to exclude, e.g., single participants this snippet can be helpful (and some more potential cleanup)</summary>

```r
# maybe participant 20 dropped out during the study
excludedParticipants = c('20')
#excludedParticipants = c('20', '7', '11' ) #11 and 7 also did not understand task 2 correctly, exclude?

#sometimes data is misclassified as numerical or simple character, so tell R: this is a factor!
ActData$TurnTaking <- as.factor(ActData$TurnTaking)
ActData$ParticipantID <- as.factor(ActData$ParticipantID)

#remove excluded participants
library(dplyr)
ActData <- filter(ActData, ! ParticipantID %in% excludedParticipants)

```


</details>


# Hypothesis Testing

Normally you want to use the gathered data to proof that a factor you evaluated has a significant effect on the outcome.

For this I recommend the following article on how to apply repeated-measures ANOVAs in R: https://www.datanovia.com/en/lessons/repeated-measures-anova-in-r/

In general, you should check perform performing paramteric test (like ANOVA or t-tests) that your data is actually normally distributed and fullfills the requirements (see website above) and otherwise use a non-parametric test should be used (*text books have an exclusion for this for large numbers (Central Limit Theorem), which often refers to 30 being a large enough number*). Otherweise check this graph for which tests might be useful (taken from the second book under Further Reading):<br>
![image](uploads/38d6fe059e5966411b0de20f3c478f9c/image.png){width=500px}


# Plotting your data

``ggpubr`` is a very versatile tool to generate nice looking plots in R (see, e.g., https://rpkgs.datanovia.com/ggpubr/)

<details><summary>Here is some example code how to create bar plots which are very configurable</summary>

```r
library(dplyr)
library(ggpubr)

library(showtext)
font_families()

ActDataGaps$TurnTaking <- recode_factor(ActDataGaps$TurnTaking, None = "None", 
InhaleOnly = "Breath", GestureOnly = "Gesture", GazeOnly = "Gaze", Full = "Full")

ActGaps_table <- ActDataGaps %>% 
  group_by(TurnTaking) %>% 
  get_summary_stats(GapTimes, type = "mean_se")

plot <- ggplot(ActGaps_table, aes(x=TurnTaking, fill=TurnTaking, y = mean*1000)) + 
  geom_bar(stat = "identity", show.legend = FALSE) +
  geom_errorbar(aes(ymin=1000*(mean-se), ymax=1000*(mean+se)), width=.3) +
  geom_signif(comparisons = list(c("Breath", "Gesture"),c("Breath", "Full")), annotation = c("*","**"), y_position = c(1000, 1100)) +
  xlab("Turn-Taking Cues") + ylab("Gap Length [ms]") +
  ylim(0, 1200) + 
  theme_light() +
  theme( text=element_text(size=8, family="serif"), 
         axis.text.x = element_text(size = 5),
         axis.text.y = element_text(size = 5, angle = 45)) + 
  scale_fill_manual(values = c("#868686", "#0073c2", "#efc000", "#cd534c", "#7aa6dc"))
print(plot)
ggsave("plots/Act-Gaps.pdf", width = 4.235, height = 6, units = "cm")
```

This script creates this graph:<br>
![image](uploads/48140956d276ed3e3dec21f9050da67e/image.png){width=300px}<br>
which could ne directly included in a Latex document with column width 4.235 cm.

</details>







# Further Reading

* A German extensive book about statistics (including a lot of hypotheses testing and some R examples): [Angewandte Statistik by Hedderich & Sachs](https://link.springer.com/book/10.1007/978-3-662-62294-0)
* A general book about study design (also containing a longer section about statistics): [Experimental Design: From User Studies to Psychophysics](https://www.taylorfrancis.com/books/mono/10.1201/b11308/experimental-design-douglas-cunningham-christian-wallraven)
* Data in R: https://moderndive.com/1-getting-started.html
* Introduction to Linear Mixed Models (Alternative to ANOVAS etc.): https://ourcodingclub.github.io/tutorials/mixed-models/
* Annotations in facets in plots: https://www.r-bloggers.com/2018/11/adding-different-annotation-to-each-facet-in-ggplot/