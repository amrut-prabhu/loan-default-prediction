nlsds <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-NSLDS-Elements.csv")
treasury <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Treasury-Elements.csv")
scorecard <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Scorecard-Elements.csv")

all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")

write.csv(all.data.elements, "~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-All-Elements.csv")

