import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor 
import importlib
from sklearn.model_selection import train_test_split
import_accuracy = getattr(importlib.import_module("scoring"), "import_accuracy")
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 2:12].copy()
df_X = pd.get_dummies(df_X)

df_y = df[df.columns[13]].copy()

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)

min_samples_leaf = [0.1, .005, .01, .00005, 0.0001, .0005, 0.001]
learning_rate = [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.3]
loss = ['ls', 'lad', 'huber', 'quantile']

model = GradientBoostingRegressor(n_estimators = 1900, max_depth = 70, random_state = 50, min_samples_split = 0.1, max_features = 'sqrt', warm_start = True)
pprint(model.get_params())
model = GridSearchCV(estimator = model, param_grid = random_grid, cv = 3, verbose=2, n_jobs = -1)
print("Fitting model")
model.fit(X_train, y_train)
pprint(model.best_params_)
print("Saving model")
joblib.dump(model, "../pklfiles/GradientBoostingRegressorGridSearchCVRepayment.pkl")
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
