import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



# データの準備、および分割
dataset = load_breast_cancer()
X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = pd.DataFrame(dataset.target, columns=['target'])
train_x, test_x, train_y, test_y = train_test_split(X, y)



# グリッドサーチ
#あらかじめパラメータの候補値を指定し、その候補パラメータを組み合わせて学習を試行することにより最適なパラメータを走査する方法。

#ランダムサーチ
#パラメータの設定範囲および試行回数を指定し、指定値範囲内から無作為に抽出したパラメータにより学習を試行することにより最適なパラメータを走査する方法。

# グリッドサーチ(パラメータ候補指定)用のパラメータ10種
paramG = {'n_estimators':[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
# ランダムサーチ(パラメータ範囲指定)用のパラメータ 1~100
paramR = {'n_estimators':np.arange(100)}

# モデル生成。上から順に、通常のランダムフォレスト、グリッドサーチ・ランダムフォレスト、
# ランダムサーチ・ランダムフォレスト。
RFC_raw  = RandomForestClassifier(random_state=0)
RFC_grid = GridSearchCV(estimator=RandomForestClassifier(random_state=0), param_grid=paramG, scoring='r2', cv=3)
RFC_rand = RandomizedSearchCV(estimator=RandomForestClassifier(random_state=0), param_distributions=paramR, scoring='r2', cv=3)


#モデリングと予測
model=RandomForestRegressor(n_estimators=1000)
model.fit(train_x,train_y)
y_pred=model.predict(test_x)

#結果の表示
testUpDown=[]
for test in test_y:
  if test>str(0):
    testUpDown.append(1)
  else:
    testUpDown.append(-1)
predUpDown=[]
for pred in y_pred:
  if pred>0:
    predUpDown.append(1)
  else:
    predUpDown.append(-1)
print("確率："+str(metrics.accuracy_score(testUpDown,predUpDown)*100)+"%")







# 各モデルに学習を行わせる。
RFC_raw.fit (train_x, train_y.values.ravel())
RFC_grid.fit(train_x, train_y.values.ravel())
RFC_rand.fit(train_x, train_y.values.ravel())

# 各モデルの n_estimators パラメータの確認。
print('通常のランダムフォレストモデルにおける n_estimators         :  %d'  %RFC_raw.n_estimators)
print('グリッドサーチ・ランダムフォレストモデルにおける n_estimators   :  %d'  %RFC_grid.best_estimator_.n_estimators)
print('ランダムサーチ・ランダムフォレストモデルにおける n_estimators  :  %d'  %RFC_rand.best_estimator_.n_estimators)

###出力結果###
'''
通常のランダムフォレストモデルにおける n_estimators           :  10
グリッドサーチ・ランダムフォレストモデルにおける n_estimators     :  100
ランダムサーチ・ランダムフォレストモデルにおける n_estimators    :  66
'''
# 各モデルにより算出される予測値
print('通常のランダムフォレストモデルによる予測値         :  %.3f'  %r2_score(test_y, RFC_raw.predict(test_x)))
print('グリッドサーチ・ランダムフォレストモデルによる予測値   :  %.3f'  %r2_score(test_y, RFC_grid.predict(test_x)))
print('ランダムサーチ・ランダムフォレストモデルによる予測値  :  %.3f'  %r2_score(test_y, RFC_rand.predict(test_x)))

###出力結果###
'''
通常のランダムフォレストモデルによる予測値           :  0.762
グリッドサーチ・ランダムフォレストモデルによる予測値     :  0.881
ランダムサーチ・ランダムフォレストモデルによる予測値    :  0.851
'''