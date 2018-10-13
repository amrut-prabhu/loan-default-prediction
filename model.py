import numpy as np
import pandas as pd

df = pd.read_csv('data/model_data.csv',sep=',')

print("Number of data points: %d \n" % df.shape[0])

print("Number of defaults:")
counts = df.DEFAULT.value_counts()
print (counts)

# from ggplot import *
# ggplot(df,aes("DEFAULT")) + geom_histogram(binwidth=1) + xlab("Defaulted?") + ylab("Number of people")


# Drop string field and id field
df.drop('INSTNM', axis=1, inplace=True)
df.drop('UNITID', axis=1, inplace=True)
print("The", df.shape[1], "features (and their data types) are: \n ", df.dtypes, "\n")


# Partition the features from the class to predict
df_X = df[df.columns[df.columns != 'DEFAULT']].copy()
df_y = df['DEFAULT'].copy()

# df['DEFAULT'].value_counts().plot(kind = 'bar', title = 'Distribution of classes')


from sklearn.model_selection import train_test_split

# (random_state): we use a fixed random seed so we get the same results every time.
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=0)
print ("\nNumber of training instances: ", len(X_train), "\nNumber of test instances: ", len(X_test))


print("\nDataset description: \n", X_train.describe())


from sklearn import datasets, metrics
from sklearn.linear_model import Perceptron
from sklearn import neighbors
from sklearn.linear_model import LogisticRegression


classifier = Perceptron(tol=None, max_iter =1000)

classifier.fit(X_train, y_train)

expected = y_test
predicted = classifier.predict(X_test)

print("\n\n******************************RESULTS******************************\n")
print("The classification score for linear classification is %.5f\n" % classifier.score(X_test, y_test))

# print("Classification report for classifier %s:\n%s" % (classifier, metrics.classification_report(expected, predicted)))
# print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

for i in range(1,6):
    knn = neighbors.KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train, y_train)

    expected = y_test
    predicted = knn.predict(X_test)

    print("The classification score for", i, "-NN is %.5f\n" % knn.score(X_test, y_test))




model = LogisticRegression(C=1e20)
model.fit(X_train, y_train)
# print('The learned weights are {} {}'.format(model.intercept_, model.coef_))

expected = y_test
predicted = model.predict(X_test)
print("The classification accuracy for logistic regression is %.5f\n" % (((predicted == y_test).mean())))