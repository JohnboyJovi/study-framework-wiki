Here are some hints and ideas how to evaluate the gathered data.

# Software

One possibility is to use RStudio. (Install r: https://cran.rstudio.com/, and then install RStudio: https://posit.co/download/rstudio-desktop/)

All of the scripts below are for RStudio, but for example also 🔴*add the program used by Sevince*🔴 can be used.

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

For this I recommend the following article on how to apply repeated-measures ANOVAs in R, 





# Further Reading

* A German extensive book about statistics (including a lot of hypotheses testing and some R examples): [AngewandteStatistikBuch.pdf](uploads/75c2870060115d3ec2b6aa4e6555f81f/AngewandteStatistikBuch.pdf)
* A general book about study design (also containing a longer section about statistics): [Experimental_Design_From_User_Studies_to_Psychophysics.pdf](uploads/513f842a02ad2b740f59a7a46e761dbf/Experimental_Design_From_User_Studies_to_Psychophysics.pdf)
