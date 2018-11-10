import pandas as pd;
import os;

# x = input("Enter x:");

dir = ".\\Predictions";
for file in os.listdir(dir):
    if file.endswith(".csv"):
        pathToFile = os.path.join(dir, file);
        print("Processing file: ", file);
        df = pd.read_csv(pathToFile).T;
        df = df.drop(['Unnamed: 0']);
        df.columns = ['Actual', 'Predicted', 'Error']
        df.to_csv(pathToFile, header=True);
