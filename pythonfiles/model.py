import numpy as np
import pandas as pd

df = pd.read_csv('data/Merged Dataset after smoothing.csv',sep=',')

print("Number of data points: %d \n" % df.shape[0])

print("Number of defaults:")
counts = df.MD_EARN_WNE_P6.value_counts()
print (counts)

# from ggplot import *
# ggplot(df,aes("DEFAULT")) + geom_histogram(binwidth=1) + xlab("Defaulted?") + ylab("Number of people")


# Drop string field and id field
df.drop('INSTNM', axis=1, inplace=True)
df.drop('UNITID', axis=1, inplace=True)
df.drop('CITY', axis=1, inplace=True)
df.drop('STABBR', axis=1, inplace=True)
print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")


# Partition the features from the class to predict
df_X = df[df.columns[df.columns != 'MD_EARN_WNE_P6']].copy()
df_y = df['MD_EARN_WNE_P6'].copy()

# df['DEFAULT'].value_counts().plot(kind = 'bar', title = 'Distribution of classes')


from sklearn.model_selection import train_test_split

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))


print("\nDataset description: \n", X_train.describe())


from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

y_pred_train = regr.predict(X_train)
print(y_train.values)
print(y_pred_train)
print(np.diff(y_train.values, y_pred_train))
