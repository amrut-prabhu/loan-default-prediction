import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import RegressorChain 
from sklearn.multioutput import MultiOutputRegressor 
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 1:12].copy()
df_X = pd.get_dummies(df_X)

df_y1 = df.iloc[:, 12:15].copy()
df_y1 = pd.get_dummies(df_y1)

df_y2 = df.iloc[:, 15:19].copy()
df_y2 = pd.get_dummies(df_y2)

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y1, test_size=0.2, random_state=0)

def accuracy(model, X_test, y_test):
	predictions = model.predict(X_test)
	print(model.score(X_test, y_test))
	errors = np.abs(predictions - y_test)
	mape = 100 * (errors / y_test)
	for col in mape:
	    accuracy = 100 - np.mean(mape[col])
	    print('Accuracy:', round(accuracy, 2), '%.')

model1 = RegressorChain(RandomForestRegressor(n_estimators = 1650, max_depth = 80, min_samples_split = 0.1, max_features = 'sqrt', bootstrap = False, n_jobs = -1, random_state = 1), cv = 3)
model2 = MultiOutputRegressor(RandomForestRegressor(n_estimators = 1650, max_depth = 80, min_samples_split = 0.1, max_features = 'sqrt', bootstrap = False, n_jobs = -1, random_state = 2))
model1.fit(X_train, y_train)
joblib.dump(model1, "RegressorChainRandomForestRegressorEarningsNew.pkl")
print("Model 1: ");
accuracy(model1, X_test, y_test)
model2.fit(X_train, y_train)
joblib.dump(model2, "MultipleOutputRandomForestRegressorEarningsNew.pkl")
print("Model 2: ");
accuracy(model2, X_test, y_test)

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y2, test_size=0.2, random_state=0)

model1.fit(X_train, y_train)
joblib.dump(model1, "RegressorChainRandomForestRegressorRepaymentNew.pkl")
print("Model 3: ");
accuracy(model1, X_test, y_test)
model2.fit(X_train, y_train)
joblib.dump(model2, "MultipleOutputRandomForestRegressorRepaymentNew.pkl")
print("Model 4: ");
accuracy(model2, X_test, y_test)
