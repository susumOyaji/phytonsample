import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier # ランダムフォレスト用
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score



'''
教師データをつくる
まずは一番面倒な株価の調整後終値から教師データを作るまでのコードを用意します。
これは終値のリストを渡すと train_X と train_y が返るようにすれば良いでしょう。
'''
def train_data(arr):
    train_X = []
    train_y = []
    # 30 日間のデータを学習、 1 日ずつ後ろにずらしていく
    for i in np.arange(-30, -15):
        s = i + 14 # 14 日間の変化を素性にする
        feature = arr.ix[i:s]
        if feature[-1] < arr[s]: # その翌日、株価は上がったか？
            train_y.append(1) # YES なら 1 を
        else:
            train_y.append(0) # NO なら 0 を
        train_X.append(feature.values)
    # 上げ下げの結果と教師データのセットを返す
    return np.array(train_X), np.array(train_y)
    #これで train_X (教師データの配列) と train_y (それに対する 1 か 0 かのラベル) が返ってきます。

'''
リターンインデックスを算出する
さて、生の株価データそのままですと、会社ごとに価格帯も全然ちがいますから教師データとしてはちょっと使いづらいです。正規化しても良いのですが、ここは資産価値の変化をあらわすリターンインデックスに注目しましょう。算出方法は前回も書きましたがこのように pandas で求まります。
'''
returns = pd.Series(close).pct_change() # 騰落率を求める
ret_index = (1 + returns).cumprod() # 累積積を求める
ret_index[0] = 1  # 最初の値を 1.0 にする

'''
リターンインデックスの変化を決定木に学習させる
さてここからがキモです。
こうして求まったリターンインデックスから教師データを抽出し分類器に学習させます。
'''
# リターンインデックスを教師データを取り出す
train_X, train_y = train_data(ret_index)
# 決定木のインスタンスを生成
clf = tree.DecisionTreeClassifier()
# 学習させる
clf.fit(train_X, train_y)















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