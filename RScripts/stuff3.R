treasury <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Treasury-Elements.csv")
treasury2 <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Treasury-Elements.csv")
summary(treasury)

library(tibble)
add_column(treasury, treasury2$COUNT_NWNE_P10, .after = treasury$UNEMP_RATE)

treasury2[18] <- as.numeric(treasury2$COUNT_NWNE_P10) / (as.numeric(treasury2$COUNT_NWNE_P10) + as.numeric(treasury2$COUNT_WNE_P10))
treasury[12] <- treasury2[18]
summary(treasury)
names(treasury)[38] <- "PCT_NWNE_P9"
treasury[39:41] <- NULL

treasury$COUNT_NWNE_P9 <- as.numeric(treasury2$COUNT_NWNE_P9) / (as.numeric(treasury2$COUNT_NWNE_P9) + as.numeric(treasury2$COUNT_WNE_P9))


install.packages("tidyverse")