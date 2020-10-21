# ## 2. 線形回帰・単回帰モデルの実装

# ### 2.1 ライブラリの読み込み
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_style("ticks")

# ### 2.2 データの読み込み
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

print(df.head())

# 可視化
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df.RM, y=df.MEDV, alpha=0.7)
plt.show()

# ### 2.3 データの準備
x = df['RM']
X = np.array(x).reshape(-1, 1)
y = df['MEDV']

print('-'*10 + '特徴量とターゲットに分割' + '-'*10)
print('X:', X.shape)
print('y:', y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print('元データ', X.shape)
print('学習用データ', X_train.shape)
print('テスト用データ', X_test.shape)

# ### 2.4 単回帰モデルの作成と評価
lm = LinearRegression()
lm.fit(X_train, y_train)

print('Train Score：{:.2f}' .format(lm.score(X_train, y_train)))
print('Test Score：{:.2f}' .format(lm.score(X_test, y_test)))
print('バイアス', lm.intercept_)
print('重み', lm.coef_)

# ### 2.5. 学習結果の可視化
y_pred = lm.predict(X_test)

plt.figure(figsize=(10, 6))
sns.scatterplot(X.reshape(len(X), ), y, alpha=0.7)
sns.lineplot(x=X_test.reshape(len(X_test), ), y=y_pred, linewidth=3, label='Simple Regression Model')
plt.xlabel('RM')
plt.ylabel('MEDV')
plt.show()