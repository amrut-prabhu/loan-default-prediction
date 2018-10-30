nlsds <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-NSLDS-Elements.csv")
summary(nlsds[1:118])

nlsds <- nlsds2nlsds

names(nlsds_redacted)
nlsds[2:3] <- NULL

nlsds[97:98] <- NULL
loadhistory(file = ".Rhistory")
history(reverse = FALSE)

CUML_DEBT_P90 