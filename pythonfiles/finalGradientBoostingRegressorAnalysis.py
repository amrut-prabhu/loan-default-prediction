import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import RegressorChain 
from sklearn.multioutput import MultiOutputRegressor 
from sklearn.model_selection import train_test_split


pd.set_option('display.max_columns', 500)

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 2:13].copy()
df_X = pd.get_dummies(df_X)

df_y1 = df.iloc[:, 13:16].copy()
df_y1 = pd.get_dummies(df_y1)

df_y2 = df.iloc[:, 16:20].copy()
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

model = GradientBoostingRegressor(n_estimators = 1900, max_depth = 70, random_state = 50, learning_rate = 0.1, min_samples_split = 0.1, max_features = 'sqrt', loss = 'lad', warm_start = True, min_samples_leaf = 0.0005)
model1 = RegressorChain(model, cv = 3)
model2 = MultiOutputRegressor(model, n_jobs = -1)
model1.fit(X_train, y_train)
joblib.dump(model1, "RegressorChainGradientBoostingRegressorEarningsNew.pkl")
print("Model 1: ");
accuracy(model1, X_test, y_test)
model2.fit(X_train, y_train)
joblib.dump(model2, "MultipleOutputGradientBoostingRegressorEarningsNew.pkl")
print("Model 2: ");
accuracy(model2, X_test, y_test)

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y2, test_size=0.2, random_state=0)

model1.fit(X_train, y_train)
joblib.dump(model1, "RegressorChainGradientBoostingRegressorRepaymentNew.pkl")
print("Model 3: ");
accuracy(model1, X_test, y_test)
model2.fit(X_train, y_train)
joblib.dump(model2, "MultipleOutputGradientBoostingRegressorRepaymentNew.pkl")
print("Model 4: ");
accuracy(model2, X_test, y_test)
