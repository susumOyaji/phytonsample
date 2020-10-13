import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

#%matplotlib inline






# ライブラリの読み込み
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split




df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv',sep=";",encoding="utf-8")
df.head()

train_x = df.drop(['quality'], axis=1)
train_y = df['quality']
(train_x, test_x ,train_y, test_y) = train_test_split(train_x, train_y, test_size = 0.3)

clf = RandomForestClassifier(max_depth=30, n_estimators=30, random_state=42)
clf.fit(train_x, train_y)#訓練用データで学習

y_pred = clf.predict(test_x)#テスト用データの予測
accuracy = accuracy_score(test_y, y_pred)
print('Accuracy: {}'.format(accuracy))







# irisデータの読み込み
iris = datasets.load_iris()

# 特徴量とターゲットの取得
data       = iris['data']
target     = iris['target']

#学習データをテストデータを分割
train_data,test_data,train_target,test_target = train_test_split(data,target,test_size=0.5)

#モデル学習
model = RandomForestClassifier(n_estimators=100)
model.fit(train_data, train_target)

# 正解率を表示
model.score(test_data, test_target)