import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
# Pandas読み込み
import pandas as pd

# csvのファイル名
csv_path = 'foo.csv'
# データフレーム読込
#data = pd.read_csv(csv_path, header=0)



data = np.loadtxt('foo.csv', delimiter=',', dtype=float)
print(data)

#data.columns = ["day_no","class","score1"]  #カラム名を付ける
#data.index = [11, 12, 13, 14, 15,16]  #インデックス名を付ける
#labels = data['day_no'] # 目的変数を取り出す

# 説明変数の格納
x = data[:,0:2] # 目的変数を取り出す,すべての行の0~1列
print('説明変数を出力\n',x)

#目的変数の格納
y = data[:, 2:3].ravel()
print("目的変数を出力\n", y)


#学習用データと評価用データに分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print("学習用の目的変数を出力\n", y_train)
print("学習用の説明変数を出力\n", x_train)
print("評価用の目的変数を出力\n", y_test)
print("評価用の説明変数を出力\n", x_test)



from sklearn.ensemble import RandomForestRegressor
#モデルに決定木を選択
clf = tree.DecisionTreeClassifier()
#clf = RandomForestRegressor()

#学習
clf.fit(x_train, y_train)


#評価用データを使って予測
predict = clf.predict(x_test)
print("評価結果を出力\n", predict)
print("正解率を出力\n", accuracy_score(y_test, predict))






'''
features = preprocessing.minmax_scale(data[:,1:])  # 説明変数を取り出した上でスケーリング
#print(features)
# X,yをそれぞれランダムに、学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
x_train, x_test, y_train, y_test = train_test_split(features, labels.ravel(), test_size=0.8) # トレーニングデータとテストデータに分割




# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor()
regr.fit(x_train, y_train)
regr.predict(x_test)#テストデータを使った予測です。



#正解率（accuracy）、適合率（precision）、再現率（recall）を出したい場合は、
from sklearn.metrics import accuracy_score, precision_score, recall_score
#from sklearn.ensemble import RandomForestClassifier

predict = regr.predict(x_test)
print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))


#print(x_train)
#print(y_train)


#print('')



# テストデータのyの予測値を求める
y_predicted = regr.predict(x_test)

# 実際のyの値と予測値を比較して、テストデータに関するR2決定係数を確認する
from sklearn import metrics
R2test = metrics.r2_score(y_test, y_predicted)
print(R2test)
'''




#print(clf.predict(x_test))

#from sklearn.metrics import accuracy_score, precision_score, recall_score

#predict = clf.predict(x_test)
#print(accuracy_score(y_test, predict), precision_score(y_test, predict), recall_score(y_test, predict))