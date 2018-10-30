import numpy as np
import pandas as pd
import threading
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn import cross_validation, metrics   #Additional scklearn functions
from sklearn.grid_search import GridSearchCV   #Perforing grid searc
h
df = pd.read_csv('data/New Datasets/multi-model-data-elements.csv',sep=',')
print("Number of data points: %d \n" % df.shape[0])

print(df.columns.values);

# Drop string field and id field
# print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")
# Partition the features from the class to predict
df_X = df.iloc[:, 2:12].copy()
df_X = pd.get_dummies(df_X)
print(df_X.head())

def func(df_X, df, i):

    df_y = df[df.columns[i]].copy()
    print(df_y.head())

# (random_state): we use a fixed random seed so we get the same results every time.
    X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
    print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))

# print("\nDataset description: \n", X_train.describe())
    print("Creating model")
    model = RandomForestRegressor(n_estimators = 1000)
    print("Fitting model")
    model.fit(X_train, y_train)
    print("Saving model")
    joblib.dump(model, "RandomForestRegressor(1000)forcolno" + str(i) + ".pkl")
    print("Predicting model")
    predictions = model.predict(X_test)
    
    print("Scoring model (R^2)")
    print(model.score(X_test, y_test))
    errors = abs(predictions - y_test)
    print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / y_test)
# Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

# print("Loading model")
# model = joblib.load("RegressorChain.pkl")
    print(str(X_train[0:1])) 
    print(str(y_train[0:1]))
    print(model.predict(X_train[0:1]))
    print(str(X_test[0:1]))
    print(str(y_test[0:1]))
    print(model.predict(X_test[0:1]))

# Print out the mean absolute error (mae)

for i in range(12, 20):
    
    print("Column number: " + str(i))
    func(df_X, df, i);

   
