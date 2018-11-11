import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, make_scorer, mean_squared_error
import importlib
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import_accuracy = getattr(importlib.import_module("scoring"), "import_accuracy")

def accuracy(y_test, predictions):
	errors = abs(predictions - y_test)
	mape = 100 * (errors / y_test)
	accuracy = 100 - np.mean(mape)
	return accuracy

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 2:12].copy()
df_X = pd.get_dummies(df_X)

df_y = df[df.columns[13]].copy()

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)

n_estimators = [int(x) for x in np.linspace(start = 1000, stop = 2000, num = 20)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(20, 100, num = 10)]
max_depth.append(None)
min_samples_split = [0.01, 0.05, 0.1, 0.2, 0.3]

error_rate = []
model = RandomForestRegressor(warm_start=True, oob_score=True, max_depth = 80, min_samples_split = 0.1, max_features = 'sqrt', bootstrap = True, n_jobs = -1, random_state = 1)

for i in n_estimators: 
	model.set_params(n_estimators=i)
        model.fit(df_X, df_y)

        # Record the OOB error for each `n_estimators=i` setting.
        oob_error = 1 - model.oob_score_
        error_rate.append((i, oob_error))

print(error_rate)

#grid_obj = GridSearchCV(scoring = make_scorer(import_accuracy), estimator = model, n_jobs = -1,  param_grid = {'n_estimators': n_estimators}, verbose = 2)
#grid_obj.fit(X_train, y_train)
#scores = grid_obj.cv_results_['mean_test_score'].reshape(len(n_estimators))
#print(scores)

#plt.figure(figsize=(8, 6))
#plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
#plt.imshow(scores, interpolation='nearest', cmap=plt.cm.hot)
#plt.xlabel('max_depth')
#plt.ylabel('min_samples_split')
#plt.colorbar()
#plt.xticks(np.arange(len(max_depth)), max_depth)
#plt.yticks(np.arange(len(min_samples_split)), min_samples_split)
#plt.title('Grid Search Score')
#plt.show()



