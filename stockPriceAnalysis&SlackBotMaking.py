#import vital tools
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from selenium import webdriver
import requests
import json

#reading csv file (*ETF=Exhange Traded Funds)
train=pd.read_csv("stockPriceData.csv")
train.head()