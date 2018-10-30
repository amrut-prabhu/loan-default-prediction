summary(model)
model$LOCALE <- as.numeric(as.character(model$LOCALE))
model$LOCALE[is.na(model$LOCALE)] <- 0
