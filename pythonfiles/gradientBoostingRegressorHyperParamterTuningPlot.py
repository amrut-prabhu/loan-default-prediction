import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor 
import importlib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, make_scorer, mean_squared_error
import_accuracy = getattr(importlib.import_module("scoring"), "import_accuracy")
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 2:12].copy()
df_X = pd.get_dummies(df_X)

df_y = df[df.columns[13]].copy()

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)

min_samples_leaf = [0.5, 0.2, 0.1, 0.08, 0.06, 0.04, .02, 0.01, 0.008, 0.005, 0.003, 0.001, 0.0008, 0.0005, 0.0001,.00008, 0.00001]
learning_rate = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5]
loss = ['ls', 'lad', 'huber', 'quantile']

model = GradientBoostingRegressor(n_estimators = 1900, max_depth = 70, random_state = 50, min_samples_split = 0.1, max_features = 'sqrt', warm_start = True)
grid_obj = GridSearchCV(scoring = make_scorer(import_accuracy), estimator = model, param_grid = {'min_samples_leaf': min_samples_leaf}, cv = 3, verbose=2, n_jobs = -1)
grid_obj.fit(X_train, y_train)
scores = grid_obj.cv_results_['mean_test_score'].reshape(len(min_samples_leaf))
print(scores)

#print("Scoring model (R^2)")
#print(model.score(X_test, y_test))
#errors = abs(predictions - y_test)
#print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
#mape = 100 * (errors / y_test)
# Calculate and display accuracy
#accuracy = 100 - np.mean(mape)
#print('Accuracy:', round(accuracy, 2), '%.')


