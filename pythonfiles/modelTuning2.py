import numpy as np
import pandas as pd
import threading
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingRegressor 
from pprint import pprint

df = pd.read_csv('data/New Datasets/multi-model-data-elements.csv',sep=',')
print("Number of data points: %d \n" % df.shape[0])

print(df.columns.values);

# Drop string field and id field
# print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")
# Partition the features from the class to predict
df_X = df.iloc[:, 2:12].copy()
df_X = pd.get_dummies(df_X)
print(df_X.head())

df_y = df[df.columns[12]].copy()
print(df_y.head())

from sklearn.model_selection import train_test_split

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))

from sklearn.model_selection import RandomizedSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 1000, stop = 2000, num = 100)]
learning_rate = [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.3]
# Number of features to consider at every split
max_features = ['auto', 'sqrt', 'log2', None]
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Method of selecting samples for training each tree
warm_start = [True, False]
loss = ['ls', 'lad', 'huber', 'quantile']

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'loss': loss,
               'learning_rate': learning_rate,
               'warm_start': warm_start
               }

# print("\nDataset description: \n", X_train.describe())
print("Creating model")
model = GradientBoostingRegressor(n_estimators = 1000, random_state = 50, max_features = "auto", min_samples_leaf = 1)
pprint(model.get_params())
model = RandomizedSearchCV(estimator = model, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
print("Fitting model")
model.fit(X_train, y_train)
pprint(model.best_params_)
print("Saving model")
joblib.dump(model, "RandomForestRegressorRandomizedSearchCV.pkl")
#print("Loading model")
#model = joblib.load("RandomForestRegressor(1000)forcolnofortuning.pkl")
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

#print(str(X_train[0:1])) 
#print(str(y_train[0:1]))
#print(model.predict(X_train[0:1]))
#print(str(X_test[0:1]))
#print(str(y_test[0:1]))
#print(model.predict(X_test[0:1]))
