all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- grep("*LO_INC*", colnames(all.data.elements))
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("*DEP_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*DEP_*", colnames(all.data.elements))]
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_*", colnames(all.data.elements))]
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP\_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP\_*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(all.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(all.data.elements))]
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(male.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(male.data.elements))]
all.data.elements <- all.data.elements[ , -grep("COMPL_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("NONCOM_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LOAN*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FEMALE", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MARRIED", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEPENDENT", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("VETERAN", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FAMINC", colnames(all.data.elements))]
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(male.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(male.data.elements))]
all.data.elements <- all.data.elements[ , -grep("COMPL_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("NONCOM_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LOAN*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FEMALE", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MARRIED", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEPENDENT", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("VETERAN", colnames(all.data.elements))]
all.data.elements[17] <- NULL
all.data.elements[18] <- NULL
all.data.elements[19:21] <- NULL
all.data.elements[19] <- NULL
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(male.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(male.data.elements))]
all.data.elements <- all.data.elements[ , -grep("COMPL_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("NONCOM_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LOAN*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FEMALE", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MARRIED", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEPENDENT", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("VETERAN", colnames(all.data.elements))]
all.data.elements[17] <- NULL
all.data.elements[18] <- NULL
all.data.elements[19:21] <- NULL
all.data.elements[19] <- NULL
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(male.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(male.data.elements))]
all.data.elements <- all.data.elements[ , -grep("COMPL_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("NONCOM_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LOAN*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FEMALE", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MARRIED", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEPENDENT", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("VETERAN", colnames(all.data.elements))]
all.data.elements[17] <- NULL
all.data.elements[18] <- NULL
all.data.elements[19:21] <- NULL
all.data.elements[18] <- NULL
all.data.elements <- all.data.elements[ , -grep("PCT_BA", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("GRAD_PROF", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LN_MEDIAN", colnames(all.data.elements))]
all.data.elements$COUNT_NWNE_P10 <- as.numeric(all.data.elements$COUNT_NWNE_P10) / (as.numeric(all.data.elements$COUNT_NWNE_P10) + as.numeric(all.data.elements$COUNT_WNE_P10))
names(treasury)[27] <- "PCT_NWNE_P10"
names(all.data.elements)[27] <- "PCT_NWNE_P10"
all.data.elements[28] <- NULL
all.data.elements <- all.data.elements[ , -grep("MN_EARN_WNE_P10", colnames(all.data.elements))]
all.data.elements[29:33] <- NULL
all.data.elements.temp <- all.data.elements
all.data.elements <- all.data.elements[ , -grep("COUNT_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("PCT_NWNE_P10.1", colnames(all.data.elements))]
all.data.elements.temp <- all.data.elements
all.data.elements <- all.data.elements[ , -grep("*INDEP0_INC1", colnames(all.data.elements))]
library(tibble)
add_column(low.inc.data.elements, all.data.elements[grep("INC1", colnames(all.data.elements))])
add_column(low.inc.data.elements, all.data.elements[grep("MN_EARN_WNE_INC1_P10", colnames(all.data.elements))])
library(tibble)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10, .after = low.inc.data.elements$LO_INC_DEBT_MDN)
low.inc.data.elements$MN_EARN_WNE_INC1_P10 <- all.data.elements$MN_EARN_WNE_INC1_P10
all.data.elements$MN_EARN_WNE_INC1_P10 <- NULL
all.data.elements <- all.data.elements[ , -grep("*PCT10*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT25*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT75*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT90*", colnames(all.data.elements))]
low.inc.data.elements$MN_EARN_WNE_INC1_P6 <- all.data.elements$MN_EARN_WNE_INC1_P6
all.data.elements$MN_EARN_WNE_INC1_P6 <- NULL
mid.inc.data.elements$MN_EARN_WNE_INC2_P6 <- all.data.elements$MN_EARN_WNE_INC2_P6
all.data.elements$MN_EARN_WNE_INC2_P6 <- NULL
mid.inc.data.elements$MN_EARN_WNE_INC2_P10 <- all.data.elements$MN_EARN_WNE_INC2_P10
all.data.elements$MN_EARN_WNE_INC2_P10 <- NULL
high.inc.data.elements$MN_EARN_WNE_INC3_P10 <- all.data.elements$MN_EARN_WNE_INC3_P10
all.data.elements$MN_EARN_WNE_INC3_P10 <- NULL
high.inc.data.elements$MN_EARN_WNE_INC3_P6 <- all.data.elements$MN_EARN_WNE_INC3_P6
all.data.elements$MN_EARN_WNE_INC3_P6 <- NULL
dep.inc.data.elements$MN_EARN_WNE_INDEP0_P6 <- all.data.elements$MN_EARN_WNE_INDEP0_P6
all.data.elements$MN_EARN_WNE_INDEP0_P6 <- NULL
all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")
low.inc.data.elements <- all.data.elements[grep("*LO_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*LO_INC*", colnames(all.data.elements))]
high.inc.data.elements <- all.data.elements[grep("*HI_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*HI_INC*", colnames(all.data.elements))]
mid.inc.data.elements <- all.data.elements[grep("*MD_INC*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*MD_INC*", colnames(all.data.elements))]
dep.data.elements <- all.data.elements[grep("DEP_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEP_", colnames(all.data.elements))]
indep.data.elements <- all.data.elements[grep("IND_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("IND_", colnames(all.data.elements))]
male.data.elements <- all.data.elements[grep("MALE_", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MALE_", colnames(all.data.elements))]
female.data.elements <- male.data.elements[grep("FEMALE_", colnames(male.data.elements))]
male.data.elements <- male.data.elements[ , -grep("FEMALE_", colnames(male.data.elements))]
all.data.elements <- all.data.elements[ , -grep("COMPL_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("NONCOM_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LOAN*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("FEMALE", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("MARRIED", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("DEPENDENT", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("VETERAN", colnames(all.data.elements))]
all.data.elements[17] <- NULL
all.data.elements[18] <- NULL
all.data.elements[19:21] <- NULL
all.data.elements[18] <- NULL
all.data.elements <- all.data.elements[ , -grep("PCT_BA", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("GRAD_PROF", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("LN_MEDIAN", colnames(all.data.elements))]
all.data.elements$COUNT_NWNE_P10 <- as.numeric(all.data.elements$COUNT_NWNE_P10) / (as.numeric(all.data.elements$COUNT_NWNE_P10) + as.numeric(all.data.elements$COUNT_WNE_P10))
names(treasury)[27] <- "PCT_NWNE_P10"
names(all.data.elements)[27] <- "PCT_NWNE_P10"
all.data.elements[28] <- NULL
all.data.elements <- all.data.elements[ , -grep("MN_EARN_WNE_P10", colnames(all.data.elements))]
all.data.elements[29:33] <- NULL
all.data.elements.temp <- all.data.elements
all.data.elements <- all.data.elements[ , -grep("COUNT_*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("PCT_NWNE_P10.1", colnames(all.data.elements))]
all.data.elements.temp <- all.data.elements
all.data.elements <- all.data.elements[ , -grep("*INDEP0_INC1", colnames(all.data.elements))]
library(tibble)
add_column(low.inc.data.elements, all.data.elements[grep("INC1", colnames(all.data.elements))])
add_column(low.inc.data.elements, all.data.elements[grep("MN_EARN_WNE_INC1_P10", colnames(all.data.elements))])
library(tibble)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10)
add_column(low.inc.data.elements, all.data.elements$MN_EARN_WNE_INC1_P10, .after = low.inc.data.elements$LO_INC_DEBT_MDN)
low.inc.data.elements$MN_EARN_WNE_INC1_P10 <- all.data.elements$MN_EARN_WNE_INC1_P10
all.data.elements$MN_EARN_WNE_INC1_P10 <- NULL
all.data.elements <- all.data.elements[ , -grep("*PCT10*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT25*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT75*", colnames(all.data.elements))]
all.data.elements <- all.data.elements[ , -grep("*PCT90*", colnames(all.data.elements))]
low.inc.data.elements$MN_EARN_WNE_INC1_P6 <- all.data.elements$MN_EARN_WNE_INC1_P6
all.data.elements$MN_EARN_WNE_INC1_P6 <- NULL
mid.inc.data.elements$MN_EARN_WNE_INC2_P6 <- all.data.elements$MN_EARN_WNE_INC2_P6
all.data.elements$MN_EARN_WNE_INC2_P6 <- NULL
mid.inc.data.elements$MN_EARN_WNE_INC2_P10 <- all.data.elements$MN_EARN_WNE_INC2_P10
all.data.elements$MN_EARN_WNE_INC2_P10 <- NULL
high.inc.data.elements$MN_EARN_WNE_INC3_P10 <- all.data.elements$MN_EARN_WNE_INC3_P10
all.data.elements$MN_EARN_WNE_INC3_P10 <- NULL
high.inc.data.elements$MN_EARN_WNE_INC3_P6 <- all.data.elements$MN_EARN_WNE_INC3_P6
all.data.elements$MN_EARN_WNE_INC3_P6 <- NULL
dep.data.elements$MN_EARN_WNE_INDEP0_P6 <- all.data.elements$MN_EARN_WNE_INDEP0_P6
all.data.elements$MN_EARN_WNE_INDEP0_P6 <- NULL
dep.data.elements$MN_EARN_WNE_INDEP0_P10 <- all.data.elements$MN_EARN_WNE_INDEP0_P10
all.data.elements$MN_EARN_WNE_INDEP0_P10 <- NULL
indep.data.elements$MN_EARN_WNE_INDEP1_P10 <- all.data.elements$MN_EARN_WNE_INDEP1_P10
all.data.elements$MN_EARN_WNE_INDEP1_P10 <- NULL
indep.data.elements$MN_EARN_WNE_INDEP1_P6 <- all.data.elements$MN_EARN_WNE_INDEP1_P6
all.data.elements$MN_EARN_WNE_INDEP1_P6 <- NULL
female.data.elements$MN_EARN_WNE_MALE0_P6 <- all.data.elements$MN_EARN_WNE_MALE0_P6
all.data.elements$MN_EARN_WNE_MALE0_P6 <- NULL
female.data.elements$MN_EARN_WNE_MALE0_P10 <- all.data.elements$MN_EARN_WNE_MALE0_P10
all.data.elements$MN_EARN_WNE_MALE0_P10 <- NULL
male.data.elements$MN_EARN_WNE_MALE1_P10 <- all.data.elements$MN_EARN_WNE_MALE1_P10
all.data.elements$MN_EARN_WNE_MALE1_P10 <- NULL
male.data.elements$MN_EARN_WNE_MALE1_P6 <- all.data.elements$MN_EARN_WNE_MALE1_P6
all.data.elements$MN_EARN_WNE_MALE1_P6 <- NULL
all.data.elements <- all.data.elements[ , -grep("*SD_*", colnames(all.data.elements))]
all.data.elements.temp <- all.data.elements
all.data.elements <- all.data.elements[ , -grep("*MN_EARN_WNE_*", colnames(all.data.elements))]
low.inc.data.elements$NPT41_PUB <- all.data.elements$NPT41_PUB
all.data.elements$NPT41_PUB <- NULL
mid.inc.data.elements$NPT42_PUB <- all.data.elements$NPT42_PUB
all.data.elements$NPT42_PUB <- NULL
high.inc.data.elements$NPT43_PUB <- all.data.elements$NPT43_PUB
all.data.elements$NPT43_PUB <- NULL
completers.time.data <- all.data.elements[grep("COMP_ORIG*", colnames(all.data.elements))]
repayment.time.data <- all.data.elements[grep("RPY*", colnames(all.data.elements))]
earnings25.time.data <- all.data.elements[grep("GT_25K*", colnames(all.data.elements))]
earnings28.time.data <- all.data.elements[grep("GT_28K*", colnames(all.data.elements))]
write.csv(all.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/all-data-elements.csv")
write.csv(completers.time.data, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/completers-time-data.csv")
write.csv(dep.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/dependent-data-elements.csv")
write.csv(earnings25.time.data, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/earnings25-time-data.csv")
write.csv(earnings28.time.data, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/earnings28-time-data.csv")
write.csv(female.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/female-data-elements.csv")
write.csv(low.inc.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/low-income-data-elements.csv")
write.csv(mid.inc.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/mid-income-data-elements.csv")
write.csv(high.inc.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/high-income-data-elements.csv")
write.csv(male.data.elements, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/mal-data-elements.csv")
write.csv(repayment.time.data, file="~/Documents/CS3244/loan-default-prediction/data/New datasets/repayment-time-data.csv")
