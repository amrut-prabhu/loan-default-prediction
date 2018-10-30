scorecard <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Scorecard-Elements.csv")
summary(scorecard)
scorecard[2:3] <- NULL
scorecard$INSTURL <- NULL
summary(scorecard)
scorecard[5] <- NULL
summary(scorecard)
scorecard_temp <- scorecard
scorecard[5] <- NULL
scorecard[6] <- NULL
scorecard[8] <- NULL
scorecard[9] <- NULL
scorecard[9] <- NULL
scorecard[9] <- NULL
scorecard[10] <- NULL
summary(scorecard)
summary(scorecard)
scorecard_temp <- scorecard
scorecard[12:29] <- NULL
summary(scorecard)
scorecard[31:33] <- NULL
summary(scorecard)
scorecard[13:15] <- NULL
scorecard[14] <- NULL
summary(scorecard)
summary(scorecard)
scorecard[14:30] <- NULL
summary(scorecard)
scorecard[14:25] <- NULL
summary(scorecard)
scorecard[14:25] <- NULL
summary(scorecard)
scorecard[14:19] <- NULL
summary(scorecard)
scorecard2 <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Scorecard-Elements.csv")
scorecard2$NPT4_PUB <- as.numeric(scorecard2$NPT4_PUB) + as.numeric(scorecard2$NPT4_PRIV)
summary(scorecard)
scorecard2 <- read.csv("~/Documents/CS3244/loan-default-prediction/data/College Scorecard Original/Most-Recent-Cohorts-Scorecard-Elements.csv")
scorecard2$NPT4_PUB <- abs(as.numeric(scorecard2$NPT4_PUB)) + abs(as.numeric(scorecard2$NPT4_PRIV))
scorecard[15] <- scorecard2$NPT4_PUB
summary(scorecard)
scorecard[16] <- NULL
scorecard2$NPT41_PUB <- abs(as.numeric(scorecard2$NPT41_PUB)) + abs(as.numeric(scorecard2$NPT41_PRIV))
scorecard[16] <- scorecard2$NPT4_PUB
scorecard[16] <- scorecard2$NPT41_PUB
summary(scorecard)
scorecard2$NPT42_PUB <- abs(as.numeric(scorecard2$NPT42_PUB)) + abs(as.numeric(scorecard2$NPT42_PRIV))
scorecard[17] <- scorecard2$NPT42_PUB
summary(scorecard)
scorecard2$NPT43_PUB <- abs(as.numeric(scorecard2$NPT43_PUB)) + abs(as.numeric(scorecard2$NPT43_PRIV))
scorecard[18] <- scorecard2$NPT42_PUB
summary(scorecard)
scorecard[19:26] <- NULL
scorecard[19:21] <- NULL
summary(scorecard)
scorecard2 <- scorecard
scorecard <- scorecard[, -grep("*SUPP*", colnames(scorecard))]
scorecard <- scorecard2
write.csv(nlsds, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/nlsds-data-elements.csv")


