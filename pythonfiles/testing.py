import numpy as np
import pandas as pd
from sklearn.externals import joblib
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.multioutput import MultiOutputRegressor 
#from sklearn.multioutput import MultiOutputRegressor 
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1XoV8SfvHmzaxRuDRe81OWSQu10dYTbO5',sep=',')

df_X = df.iloc[:, 2:13].copy()
df_X = pd.get_dummies(df_X)

df_y1 = df.iloc[:, 13:16].copy()
df_y1 = pd.get_dummies(df_y1)

df_y2 = df.iloc[:, 16:20].copy()
df_y2 = pd.get_dummies(df_y2)

#X_train, df_X, y_train, df_y1 = train_test_split(df_X, df_y1, test_size=0.2, random_state=0)
def accuracy(model, X_test, y_test):
	predictions = model.predict(X_test)
	print(model.score(X_test, y_test))
	errors = np.abs(predictions - y_test)
	mape = 100 * (errors / y_test)
	for col in mape:
	    accuracy = 100 - np.mean(mape[col])
	    print('Accuracy:', round(accuracy, 2), '%.')

def test(model, df_X, df_y1, num):
	accuracy(model, df_X, df_y1)
	predictions = pd.DataFrame(model.predict(df_X))
	errors = np.abs(predictions - df_y1)
	print(type(predictions))
	print(type(errors))
	for i in range(num):
		#results = df_X.iloc[:, 0:10].values
		#results = np.append(results, df_y1.ix[:, i])
		#results = np.append(results, predictions[:, i])
		#results = np.append(results, errors.ix[:, i])
		#result_df = pd.DataFrame(results)
		df_X.join(df_y1.ix[:, i]).join(predictions.ix[:, i]).to_csv("ModelPredictions" + str(num) + str(i) +  ".csv")

#model = RandomForestRegressor(n_estimators = 1900, max_depth = 70, random_state = 50, learning_rate = 0.1, min_samples_split = 0.1, max_features = 'sqrt', loss = 'lad', warm_start = True, min_samples_leaf = 0.0005)
#model1 = MultipleOutputRegressor(model)
#model2 = MultipleOutputRegressor(model, n_jobs = -1)
#model1.fit(X_train, y_train)
model = joblib.load("RegressorChainGradientBoostingRegressorEarningsNew.pkl")
test(model, df_X, df_y1, 3)
model = joblib.load("RegressorChainGradientBoostingRegressorRepaymentNew.pkl")
test(model, df_X, df_y2, 4)
#model2.fit(X_train, y_train)
#joblib.dump(model2, "MultiplepleOutputRandomForestRegressorEarnings.pkl")
#print("Model 2: ");
#accuracy(model2, df_X, df_y1)

#X_train, df_X, y_train, df_y1 = train_test_split(df_X, df_y2, test_size=0.2, random_state=0)

#model1.fit(X_train, y_train)
#joblib.dump(model1, "MultipleOutputRegressorRandomForestRegressorRepayment.pkl")
#print("Model 3: ");
#accuracy(model1, df_X, df_y1)
#model2.fit(X_train, y_train)
#joblib.dump(model2, "MultiplepleOutputRandomForestRegressorRepayment.pkl")
#print("Model 4: ");
#accuracy(model2, df_X, df_y1)
