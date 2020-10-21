# ## 2. 線形回帰・重回帰モデルの実装
### 2.1 ライブラリの読み込み
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

sns.set()
sns.set_style("ticks")

# ### 2.2 データの読み込み
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

print(df.head())

# 散布図を使った可視化
X = df.RM
Y = df.LSTAT
Z = df.MEDV

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel('RM')
ax.set_ylabel('LSTAT')
ax.set_zlabel('MEDV')

ax.scatter(X,Y,Z, s=30, c='blue', alpha=0.2)

plt.show()

# ### 2.3 データの準備
X = df[['RM', 'LSTAT']]
y = df['MEDV']

print('-'*10 + '特徴量とターゲットに分割' + '-'*10)
print('X:', X.shape)
print('y:', y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print('元データ', X.shape)
print('学習用データ', X_train.shape)
print('テスト用データ', X_test.shape)

# ### 2.4 重回帰モデルの作成と評価
lm = LinearRegression()
lm.fit(X_train, y_train)


print('Train Score：{:.2f}' .format(lm.score(X_train, y_train)))
print('Test Score：{:.2f}' .format(lm.score(X_test, y_test)))

print('バイアス', lm.intercept_)
print('重み', lm.coef_)

# ### 2.5 学習結果の可視化

a1, a2 = lm.coef_ #係数
b = lm.intercept_ #切片

X = df.RM
Y = df.LSTAT
Z = df.MEDV

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X,Y,Z, s=30, c='blue', alpha=0.2)

X_3d, Y_3d = np.meshgrid(np.arange(0, 10, 1), np.arange(0, 40, 1))
Z_3d = a1 * X_3d + a2 * Y_3d + b
ax.plot_surface(X_3d, Y_3d, Z_3d)
ax.set_xlabel('RM')
ax.set_ylabel('LSTAT')
ax.set_zlabel('MEDV')

ax.view_init(elev=60, azim=45)
plt.show()