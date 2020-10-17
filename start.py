import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# Pandas読み込み
import pandas as pd

# csvのファイル名
csv_path = 'foo.csv'
# データフレーム読込
#data = pd.read_csv(csv_path, header=0)
data = np.loadtxt('foo.csv', delimiter=',')

#data.columns = ["day_no","class","score1"]  #カラム名を付ける
#data.index = [11, 12, 13, 14, 15]  #インデックス名を付ける
#labels = data['day_no'] # 目的変数を取り出す

labels = data[:, 0:1] # 目的変数を取り出す
features = preprocessing.minmax_scale(data[:, 1:])  # 説明変数を取り出した上でスケーリング
# X,yをそれぞれランダムに、学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
x_train, x_test, y_train, y_test = train_test_split(features, labels.ravel(), test_size=0.8) # トレーニングデータとテストデータに分割




# 学習データを使ってモデルを構築する
#from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor()
regr.fit(x_train, y_train)


print(x_train)
print(y_train)


print('')



# テストデータのyの予測値を求める
y_predicted = regr.predict(x_test)

# 実際のyの値と予測値を比較して、テストデータに関するR2決定係数を確認する
from sklearn import metrics
R2test = metrics.r2_score(y_test, y_predicted)
print(R2test)





#print(clf.predict(x_test))

#from sklearn.metrics import accuracy_score, precision_score, recall_score

#predict = clf.predict(x_test)
#print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))