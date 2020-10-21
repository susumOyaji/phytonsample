# ### 2.1 ライブラリのインポート
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_style("ticks")

# ### 2.2 データの読み込み
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

print(df.head())

# 散布図を使った可視化
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df.RM, y=df.MEDV, alpha=0.7)
plt.show()

# 線形回帰の直線も合わせて確認
plt.figure(figsize=(10, 6))
sns.regplot(x=df.RM, y=df.MEDV, scatter_kws={'alpha': 0.4})
plt.show()

# ### 2.3 データの準備
x = df['RM']
X = np.array(x).reshape(-1, 1)
y = df['MEDV']

print('-'*10 + '特徴量とターゲットに分割' + '-'*10)
print('X:', X.shape)
print('y:', y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# ### 2.4 多項式モデルの作成
pf = PolynomialFeatures(degree=2, include_bias=False)
X_train_2 = pf.fit_transform(X_train)
X_test_2 = pf.fit_transform(X_test)

print('元のRM：')
print(X_train[:5])
print('二乗したRM：')
print(X_train_2[:5])

# モデルの作成
lm = LinearRegression()
lm.fit(X_train_2,y_train)

# パラメータを表示
print('バイアス', lm.intercept_)
print('重み', lm.coef_)

#精度を表示
print('Train Score：{:.2f}' .format(lm.score(X_train_2, y_train)))
print('Test Score：{:.2f}' .format(lm.score(X_test_2, y_test)))

# モデルの作成
tmp = LinearRegression()
tmp.fit(X_train,y_train)

y_pred_tmp = tmp.predict(X_test)

#精度を表示
print('Train Score：{:.2f}' .format(tmp.score(X_train, y_train)))
print('Test Score：{:.2f}' .format(tmp.score(X_test, y_test)))

# ### 2.5 学習結果の可視化
X_test_a = np.array([np.sort(X_test[:,0])]).reshape(len(X_test),1)
X_test_2 = pf.fit_transform(X_test_a)

y_pred = lm.predict(X_test_2)

plt.figure(figsize=(10, 6))
sns.scatterplot(X.reshape(len(X), ), y, alpha=0.7)
sns.lineplot(x=X_test_a.reshape(len(X_test_a), ), y=y_pred, linewidth=2.5, label='poly')
sns.lineplot(x=X_test.reshape(len(X_test), ), y=y_pred_tmp, linewidth=2.5, label='linear')
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.show()