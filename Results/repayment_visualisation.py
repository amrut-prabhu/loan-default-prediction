import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

max_error = 10000;

def get_best_fit(fileName, filePath, model_used):
    df = pd.read_csv(filePath);
    total_pts = len(df); # 9725

    # Choose rows where error is less than max_error
    df = df[df['Error'] < max_error];
    print("Removed ", total_pts - len(df), " points");

    # Change to np array
    x = df['Actual'].values;
    y = df['Predicted'].values;

    # reshapre since there's only 1 feature
    x = x.reshape(-1, 1);

    regr = LinearRegression();
    regr.fit(x, y);

    maxVal = max(max(x), max(y));

    print("Equation for ", model, ": y = ", regr.coef_[0], "x + ", regr.intercept_, "\n");

    '''
    # plot some points from the results.csv file
    color = 'black';
    if model == 'MORGBR':
        color = 'pink';
    elif model == 'MORRFR':
        color = 'salmon';
    elif model == 'RCGBRN':
        color = 'wheat';
    elif model == 'RCRFR':
        color = 'paleturquoise';

    indices = np.random.randint(low=0,high=len(x), size=500);
    plot_x = [x[i] for i in indices];
    plot_y = [y[i] for i in indices];
    plt.plot(plot_x, plot_y, '.', c=color, alpha=0.5);
    '''

    return regr, maxVal;

def plot_models_results(code, models, max_val):
    # Mapping of file code to number of years that file represents
    thisdict =  {
      40: "1",
      41: "3",
      42: "5",
      43: "7"
    }

    colors = ['blue', 'black', 'purple', 'red'];

    green_patch = mpatches.Patch(color='lawngreen', label='Perfect Prediction');
    blue_patch = mpatches.Patch(color='blue', label='Gradient Boosting Multi Output Regressor');
    black_patch = mpatches.Patch(color='black', label='Random Forest Multi Output Regressor');
    purple_patch = mpatches.Patch(color='purple', label='Gradient Boosting Regressor Chain');
    red_patch = mpatches.Patch(color='red', label='Random Forest Regressor Chain');


    # plot perfit prediction line, i.e., x = y
    x_perfect = np.linspace(0, max_val, 10000);
    y_perfect = x_perfect;
    plt.plot(x_perfect, y_perfect, c='lawngreen');

    for i in range(len(models)):
        model = models[i];
        color = colors[i];

        # plot linear regression line
        # Reduce length of line as index increases so that overlapping lines are not hidden
        regr_x = np.linspace(0 + i*0.02, max_val - i*0.05, 10000);
        regr_y = model.predict(regr_x.reshape(-1, 1));
        plt.plot(regr_x, regr_y, c=color);

    plt.title("Predicted vs Actual Repayment Rates after " + thisdict[code] + " years");
    plt.xlabel('Actual Repayment Rate');
    plt.ylabel('Predicted Repayment Rate');
    plt.legend(handles=[green_patch, blue_patch, purple_patch, black_patch, red_patch]);

    plt.savefig('repayment_' + thisdict[code] + '_years_limit_' + str(max_error) + '.png', dpi=400);
    plt.show();

# Main program
prediction_results_dir = ".\\Predictions";
for code in [40, 41, 42, 43]:
    regr_models = [];
    overall_max = 0;
    print("====Processing file type: ", code);
    for model in ['MORGBR', 'MORRFR', 'RCGBRN', 'RCRFR']:
        fileName = model + "testing" + str(code);
        filePath = prediction_results_dir + "\\" + fileName + ".csv";

        regr, max_val = get_best_fit(fileName, filePath, model);

        regr_models.append(regr);
        if max_val > overall_max:
             overall_max = max_val;

    plot_models_results(code, regr_models, overall_max);

