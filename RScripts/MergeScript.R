nlsds <- read.csv("C:\\Users\\Andy\\Desktop\\collegescore\\data\\Most-Recent-Cohorts-NSLDS-Elements.csv")
treasury <- read.csv("C:\\Users\\Andy\\Desktop\\collegescore\\data\\Most-Recent-Cohorts-Treasury-Elements.csv")
scorecard <- read.csv("C:\\Users\\Andy\\Desktop\\collegescore\\data\\Most-Recent-Cohorts-Scorecard-Elements.csv")

all.data.elements <- merge(nlsds, treasury, by = "INSTNM")
all.data.elements <- merge(all.data.elements, scorecard, by = "INSTNM")


#Degree CSV
certificate.csv <- all.data.elements[all.data.elements$SCH_DEG == 1,]
associate.csv <- all.data.elements[all.data.elements$SCH_DEG == 2,]
bach.csv <- all.data.elements[all.data.elements$SCH_DEG == 3,]
graduate.csv <- all.data.elements[all.data.elements$SCH_DEG == 4,]


#Costs
# Median Family Income Independent Students, Median Earnings, Median Household Income
# Number of students by income class
# Debt Statistics
# Earnings > 25 or > 28 thousand after 6 years
# Average Net Prices

important <- c("INSTNM", "MD_FAMINC","MD_EARN_WNE_P6","MEDIAN_HH_INC",
               "LO_INC_YR2_N", "MD_INC_YR2_N","HI_INC_YR2_N",
               "DEBT_MDN", "GRAD_DEBT_MDN", "WDRAW_DEBT_MDN", "LO_INC_DEBT_MDN", "MD_INC_DEBT_MDN", "HI_INC_DEBT_MDN", 
               "GT_25K_P6.x", "GT_28K_P6.x",
               "NPT4_PUB" , "NPT4_PRIV")


certificate.csv <- certificate.csv[important]
associate.csv <- associate.csv[important]
bach.csv <- bach.csv[important]
graduate.csv <- graduate.csv[important]

write.csv(certificate.csv, "C:\\Users\\Andy\\Desktop\\collegescore\\data\\Certificate-Schools.csv")
write.csv(associate.csv, "C:\\Users\\Andy\\Desktop\\collegescore\\data\\Associate-Schools.csv")
write.csv(bach.csv, "C:\\Users\\Andy\\Desktop\\collegescore\\data\\Bach-Schools.csv")
write.csv(graduate.csv, "C:\\Users\\Andy\\Desktop\\collegescore\\data\\Grad-Schools.csv")









