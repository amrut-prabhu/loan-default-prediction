import numpy as np
import pandas as pd

df = pd.read_csv('data/New Datasets/common-data-elements-model.csv',sep=',')
df = pd.get_dummies(df)
print("Number of data points: %d \n" % df.shape[0])

print("Number of defaults:")
counts = df.MD_EARN_WNE_P10.value_counts()
print (counts)

# from ggplot import *
# ggplot(df,aes("DEFAULT")) + geom_histogram(binwidth=1) + xlab("Defaulted?") + ylab("Number of people")


# Drop string field and id field
print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")


# Partition the features from the class to predict
df_X = df[df.columns[df.columns != 'MD_EARN_WNE_P10']].copy()
df_y = df['MD_EARN_WNE_P10'].copy()

# df['DEFAULT'].value_counts().plot(kind = 'bar', title = 'Distribution of classes')


from sklearn.model_selection import train_test_split

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))


print("\nDataset description: \n", X_train.describe())

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators = 1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

errors = abs(predictions - y_test)

# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

mape = 100 * (errors / y_test)

# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

