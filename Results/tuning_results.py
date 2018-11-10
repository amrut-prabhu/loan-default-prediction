from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

# Random Forest Regressor Hyper Parameter Tuning
def plotRandomForestResults():
    plotDepthAndMinSamples()
    plotEstimators()

def plotDepthAndMinSamples():
    df = pd.read_csv('depth_samples.csv',sep=',')

    print("Number of data points = ", len(df))

    x = np.array(df['Max Depth'])
    y = np.array(df['Min samples split'])
    z = np.array(df['Accuracy'])

    fig = plt.figure(figsize=(10, 7.5)) # width x height; size in inches, 1 inch = 80 pixels

    ax = plt.axes(projection='3d')
    # ax.plot3D(x, y, z, 'gray')
    ax.scatter3D(x, y, z, c=y)
    ax.set_xlabel('Max Depth')
    ax.set_ylabel('Min samples split')
    ax.set_zlabel('Accuracy')
    ax.set_title('Variation of accuracy with Max Depth and Min Samples Split')
    ax.view_init(5, 135)

    if isSaveOn:
        plt.savefig('depth_samples.png', dpi=300)

    plt.show()

def plotEstimators():
    df = pd.read_csv('estimators.csv',sep=',')
    print("Number of data points = ", len(df))

    x = np.array(df['Number of estimators'])
    y = np.array(df['Accuracy'])

    fig = plt.figure(figsize=(7, 5))

    plt.plot(x, y, 'o', c='red')
    # plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), '-o', c='red')
    # plt.plot(x, y, 'o', c='red')
    plt.xlabel('Number of Estimators')
    plt.ylabel('Accuracy')
    plt.title('Variation of accuracy with Number of Estimators')

    if isSaveOn:
        plt.savefig('estimators.png', dpi=300)

    show()

# Gradient Boosting Regressor Hyper Parameter Tuning
def plotGradientBoostingResults():
    plotMinLeafs()
    plotLoss()

def plotMinLeafs():
    df = pd.read_csv('min-leafs.csv',sep=',')
    print("Number of data points = ", len(df))
    x = np.array(df['Min samples leaf'])
    y = np.array(df['Accuracy'])

    fig = plt.figure(figsize=(14, 5))

    plt.plot(x, y, '-o', c='blue')
    # plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), '-o', c='blue')
    # plt.plot(x, y, 'o', c='blue')
    plt.xlabel('Min samples leaf')
    plt.ylabel('Accuracy')
    plt.title('Variation of accuracy with Min samples leaf')

    if isSaveOn:
        plt.savefig('min-leafs.png', dpi=300)

    show()

def plotLoss():
    df = pd.read_csv('loss_learning-rate.csv',sep=',')
    print("Number of data points = ", len(df))

    losses = ['ls', 'lad', 'huber', 'quantile']
    x = []
    y = []
    for lossType in range(len(losses)):
        x.append(np.array([df['Learning Rate'][i] for i in range(len(df)) if df['Loss'][i] == losses[lossType]]))
        y.append(np.array([df['Accuracy'][i] for i in range(len(df)) if df['Loss'][i] == losses[lossType]]))


    fig = plt.figure(figsize=(10, 5)) # width x height; size in inches, 1 inch = 80 pixels

    # markers = ['o', '^', 's', 'd']
    markers = ['-o', '-^', '-s', '-d']
    for i in range(len(markers)):
        plt.plot(x[i], y[i], markers[i], label="{0}".format(losses[i]))

    plt.xlabel('Learning Rate')
    plt.ylabel('Accuracy')
    plt.title('Variation of accuracy with Learning Rate for different Loss functions')
    plt.legend(numpoints=1, title="Loss Function")
    plt.ylim(35, 95);

    if isSaveOn:
        plt.savefig('loss_learning-rate.png', dpi=300)

    show()

isSaveOn = True
# isSaveOn = False
plotRandomForestResults()
plotGradientBoostingResults()
