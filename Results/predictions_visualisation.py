import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def get_best_fit(fileName, filePath):
    df = pd.read_csv(filePath);

    df = filter_by_error(df, 5000);

    x = df['Actual'].values;
    y = df['Predicted'].values;

    x = x.reshape(-1, 1);

    # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5);
    model = LinearRegression();
    model.fit(x, y);

    # print(model.score(x, y));
    print("Equation: y = ", model.coef_[0], "x + ", model.intercept_, "\n");

    # plot points from the results.csv file
    plt.plot(x, y, '.', c='black')

    # plot perfit prediction line, i.e., x = y
    max_val = max(max(x), max(y));
    x_perfect = np.linspace(0, max_val, 10000);
    y_perfect = x_perfect;
    plt.plot(x_perfect, y_perfect, c='green');

    # plot linear regression line
    regr_x = np.linspace(0, max_val, 10000);
    regr_y = model.predict(regr_x.reshape(-1, 1));
    plt.plot(regr_x, regr_y, c='red');
    plt.show();

def filter_by_error(df, max_error):


# Main program
prediction_results_dir = ".\\Predictions";
for year in [6, 8, 10]:
    fileName = "earnings_" + str(year) + "_years";
    filePath = prediction_results_dir + "\\" + fileName + ".csv";
    get_best_fit(fileName, filePath);

