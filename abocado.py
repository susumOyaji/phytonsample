#ライブラリインポート
#%matplotlib inline
import numpy as np
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#データ読み込み
df = pd.read_csv("titanic.csv")
print(df)
print(df['PassengerId'])
print(df['Name'])

#scatter(df["PassengerId"],df["Pclass"])
# X,yを、それぞれランダムに学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
from sklearn.model_selection import train_test_split
X = df["PassengerId"]
y = df["Name"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
print(X_test)
print(y_test)

#scatter(X_train, Y_train)

# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestRegressor
# oob_score=True にパラメータを変更する（デフォルト値はFalse）
regr = RandomForestRegressor(oob_score=False)
regr.fit(X_train, y_train)

RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, n_jobs=1, oob_score=True, random_state=None,
           verbose=0, warm_start=False)
# oob_scoreを求める
oob_score = regr.oob_score_
print(oob_score)





# feature_importanceを求める
feature_importances = regr.feature_importances_
#print(feature_importances)


#分かりやすいようにグラフにします。
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.ylim([0, 1])
y = feature_importances
x = np.arange(len(y))
plt.bar(x, y, align="center")
plt.xticks(x, boston['feature_names'])
plt.show()

p4 = poly1d(np.polyfit(X_train,Y_train,8))
xp = np.linspace(0,20000000,50)
axes = plt.axes()
axes.set_xlim([0,20000000])
axes.set_ylim([0,6000000])
plt.scatter(X_train,Y_train)
plt.plot(xp,p4(xp),c="r")
plt.show()

'''
xp = np.linspace(0,20000000,50)
#axes = plt.axes()
axes.set_xlim([0,20000000])
axes.set_ylim([0,6000000])
plt.scatter(X_test,Y_test)
plt.plot(xp,p4(xp),c="r")
plt.show()
'''

r2 = r2_score(Y_test,p4(X_test))
print(r2)
#結果は0.6496548856957747

r2 = r2_score(Y_train,p4(X_train))
print(r2)
#結果は0.6945770505912501

