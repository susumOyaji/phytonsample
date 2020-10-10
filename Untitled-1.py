#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score

def load_dataset():
    boston = datasets.load_boston()
    print(boston['feature_names'])
    boston_df=pd.DataFrame(boston.data)
    boston_df.columns = boston.feature_names
    boston_df['PRICE'] = pd.DataFrame(boston.target)
    #print("boston_df ->" + str(boston_df))
    X_df = boston_df.drop("PRICE", axis=1)
    Y_df = boston_df.loc[:,['PRICE']]
    X_df.plot()
    Y_df.plot()
    plt.grid()
    plt.show()
    Y = boston_df.PRICE
    print("X_df ->" + str(X_df))
    print("Y ->" + str(Y))
    return X_df, Y

def execute(data, num_of_trees, max_depth):
    X_df = data[0]
    Y = data[1]
    scores=[]
    cnt=0 
    for j in range(max_depth[0], max_depth[1], 1):
        for i in range(num_of_trees[0], num_of_trees[1], 1):
            regr = RandomForestRegressor(n_estimators=i, max_depth=j, random_state=0)
            regr.fit(X_df,Y)
            score = regr.score(X_df,Y) 
            scores.append(score)
            pred_Y = regr.predict(X_df)
            #score2 = accuracy_score(Y, pred_Y)

            print("regr.fit(X_df,Y) ->" + str(regr.fit(X_df,Y)))
            print(score) # R^2
            #print(score2)

            plt.figure(1)
            plt.title('Comparison' + str(cnt))
            plt.xlabel('RM (number of rooms)', fontsize=14)
            plt.ylabel('PRICE (target)', fontsize=14)
            plt.scatter(X_df["RM"], Y, c='blue', label='Raw data')
            plt.scatter(X_df.RM, pred_Y, c='red', label='RandomForest')
            plt.legend(loc='lower right', fontsize=12)
            plt.show()
            cnt += 1

    plt.plot(scores, color="red")
    plt.xlabel('Number of Cycle', fontsize=14)
    plt.ylabel('R^2', fontsize=14)
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    num_of_trees = [5, 10] # [min, max]
    max_depth = [1, 9]     # [min, max]
    
    data=load_dataset()
    execute(data, num_of_trees, max_depth)