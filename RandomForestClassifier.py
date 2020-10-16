#1. 分類：RandomForestClassifier
#まずはデータセットを用意します。 scikit-learnのiris(アヤメ)データセットを使用します。次のように記述することで、変数「iris」にデータセットの情報が格納されます。

from sklearn import datasets
iris = datasets.load_iris()

print(iris['feature_names'])
print(iris['target_names'])
'''
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
['setosa' 'versicolor' 'virginica']
'''
print(iris['data'])
print(iris['target'])

# X,yをそれぞれランダムに、学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
from sklearn.model_selection import train_test_split
X = iris['data']
y = iris['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
clf = RandomForestClassifier()
clf.fit(X_train, y_train)


RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, n_jobs=1, oob_score=True, random_state=None,
           verbose=0, warm_start=False)


# テストデータのyの予測値を求める
y_predicted = clf.predict(X_test)

# 実際のyの値と予測値を比較して、正答率を確認する
from sklearn import metrics
accuracy = metrics.accuracy_score(y_test, y_predicted)
print(accuracy)



'''
2. 回帰：RandomForestRegressor
scikit-learnのboston(ボストン市の住宅価格)データセットを使用します。
'''
from sklearn import datasets
boston = datasets.load_boston()

#feature_name（特徴名）を見てみます。

print(boston['feature_names'])
['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO'
 'B' 'LSTAT']
''' 
各データには、各物件の人口統計に関する13の特徴量が記されています。 dataには、各物件の特徴量の値が登録されています。 targetには、各物件の価格が登録されています。 それでは、「データの特徴量の値を元に、住宅の価格を予測する」モデルを構築します。
'''

# X,yを、それぞれランダムに学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
from sklearn.model_selection import train_test_split
X = boston['data']
y = boston['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor()
regr.fit(X_train, y_train)
RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, n_jobs=1, oob_score=False, random_state=None,
           verbose=0, warm_start=False)

#各パラメータについて詳しくは、分類と同様に公式ドキュメントを参照してください。 それでは、このモデルに沿ってテストデータのy値を予測し、精度を確認します。

# テストデータのyの予測値を求める
y_predicted = regr.predict(X_test)

# 実際のyの値と予測値を比較して、テストデータに関するR2決定係数を確認する
from sklearn import metrics
R2test = metrics.r2_score(y_test, y_predicted)
print(R2test)



'''
3. その他の機能
以下に挙げるのは、Random Forestの機能の一部です。 分類でも回帰でも用いることができますが、ここではボストン市住宅価格予測の回帰モデルを例に挙げて紹介します。
'''
#・oob_score
#Random forestの各決定木を作る際に、モデル構築に用いられなかったサンプルを OOB（Out Of Bag）と言います。 この OOB をバリデーション用データのように用いて、バリデーションスコアを求めることができます。

from sklearn import datasets
boston = datasets.load_boston()

# X,yを、それぞれランダムに学習データとテストデータに分ける（学習：テスト = 0.8：0.2）
from sklearn.model_selection import train_test_split
X = boston['data']
y = boston['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

# 学習データを使ってモデルを構築する
from sklearn.ensemble import RandomForestRegressor
# oob_score=True にパラメータを変更する（デフォルト値はFalse）
regr = RandomForestRegressor(oob_score=True)
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


#・feature_importance
#Random Forest では、各変数の重要度（feature_importance）を求めることができます。 以下のようにして、13種類の特徴量がモデル構築にそれぞれどれだけ寄与したかを求めることができます。

# feature_importanceを求める
feature_importances = regr.feature_importances_
print(feature_importances)
'''
[ 0.02799019  0.00084522  0.00413129  0.00120428  0.00946862  0.60004269
  0.01418742  0.05035083  0.00475161  0.01729037  0.01621295  0.01394745
  0.23957708]
'''
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