import numpy as np
import pandas as pd
from sklearn.externals import joblib

df = pd.read_csv('data/New Datasets/multi-model-data-elements.csv',sep=',')
print("Number of data points: %d \n" % df.shape[0])

print(df.columns.values);

# Drop string field and id field
# print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")
# Partition the features from the class to predict
df_X = df.iloc[:, 1:12].copy()
df_y = df.iloc[:, 12:19].copy()
df_X = pd.get_dummies(df_X)
df_y = pd.get_dummies(df_y)

print(df_X.head())
print(df_y.head())

from sklearn.model_selection import train_test_split

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))

# print("\nDataset description: \n", X_train.describe())

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import RegressorChain 

print("Creating model")
model = RegressorChain(GradientBoostingRegressor(n_estimators = 1000))
print("Fitting model")
model.fit(X_train, y_train)
print("Saving model")
joblib.dump(model, "RegressorChainwithoutgtksand1000estimators.pkl")
#print("Loading model")
#model = joblib.load("RegressorChain.pkl")
print("Predicting model")
predictions = model.predict(X_test)
print("Scoring model")
print(model.score(X_test, y_test))
errors = np.abs(predictions - y_test)
mape = 100 * (errors / y_test)
print(type(mape))
for col in mape:
    accuracy = 100 - np.mean(mape[col])
    print('Accuracy:', round(accuracy, 2), '%.')

print(str(X_train[0:1])) 
print(str(y_train[0:1]))
print(model.predict(X_train[0:1]))
print(str(X_test[0:1]))
print(str(y_test[0:1]))
print(model.predict(X_test[0:1]))

# Print out the mean absolute error (mae)
# print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# mape = 100 * (errors / y_test)

# # Calculate and display accuracy
# accuracy = 100 - np.mean(mape)
# print('Accuracy:', round(accuracy, 2), '%.')
