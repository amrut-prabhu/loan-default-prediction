import numpy as np
import pandas as pd
from sklearn.externals import joblib
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.multioutput import MultiOutputRegressor 
#from sklearn.multioutput import MultiOutputRegressor 
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://drive.google.com/uc?export=download&id=1AsTVQvXdXRut4zaGXNhErCkrJOwcg0HH',sep=',')
df_X = df.iloc[:, 1:12].copy()
df_X = pd.get_dummies(df_X)

df_y1 = df.iloc[:, 12:15].copy()
df_y1 = pd.get_dummies(df_y1)

df_y2 = df.iloc[:, 15:19].copy()
df_y2 = pd.get_dummies(df_y2)

#X_train, df_X, y_train, df_y1 = train_test_split(df_X, df_y1, test_size=0.2, random_state=0)

def test(model, df_X, df_y1, num):
	predictions = model.predict(df_X)
	errors = np.abs(predictions - df_y1)
	for i in range(num):
		results = []
		results.append(df_y1.ix[:, i])
		results.append(predictions[:, i])
		results.append(errors.ix[:, i])
		result_df = pd.DataFrame(results)
		result_df.to_csv("RCRFRtesting" + str(num) + str(i) + ".csv")

#model = RandomForestRegressor(n_estimators = 1900, max_depth = 70, random_state = 50, learning_rate = 0.1, min_samples_split = 0.1, max_features = 'sqrt', loss = 'lad', warm_start = True, min_samples_leaf = 0.0005)
#model1 = MultipleOutputRegressor(model)
#model2 = MultipleOutputRegressor(model, n_jobs = -1)
#model1.fit(X_train, y_train)
model = joblib.load("../pklfiles/RegressorChainRandomForestRegressorEarnings.pkl")
test(model, df_X, df_y1, 3)
model = joblib.load("../pklfiles/RegressorChainRandomForestRegressorRepayment.pkl")
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
