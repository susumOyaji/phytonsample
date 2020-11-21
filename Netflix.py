#このプログラムは、Netflix株の価格を予測しようとします。

#次に、プログラム全体で使用される依存関係をインストールします。
#依存関係をインストールします
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
plt.style.use('bmh')
from datetime import datetime
#pandasのdatareaderをwebとしてインポートします。
import pandas_datareader as web


today = datetime.today().strftime("%Y-%m-%d")
#次は株価を取得していきます。今回は2020年の1月1日から本日までの株式情報を取得して行きましょう。
sony_stock = web.DataReader("SNE",data_source="yahoo",start="2012-01-01",end=today)
#データファイルを変数に格納し、データの最初の6行を出力します。
#df = pd.read_csv('NFLX_Stock.csv')
df = sony_stock
df.head(6)


#データを視覚化します。Sonyの終値がグラフでどのように見えるかを見たいです。
plt.figure(figsize=(18,8))
plt.title('Sony', fontsize = 18)
plt.xlabel('Days', fontsize= 18)
plt.ylabel('Close Price USD ($)', fontsize = 18)
plt.plot(df['Adj Close'])
plt.show()


#ここで、Sonyの終値のみを取得してデータフレームに保存し、画像を印刷したいと思います。
df = df[['Adj Close']]
df.head(4)


# 将来の「x」日を予測する変数を作成します。
# 次に、ターゲット変数または従属変数を格納するための新しい列を作成します。
# これは本質的に、「x」日上にシフトされた終値です。次に、最後の4行のデータを出力します。
#Create a variable to predict 'x' days out into the future
future_days = 25
#Create a new column (the target or dependent variable) shifted 'x' units/days up
df['Prediction'] = df[['Adj Close']].shift(-future_days)
#print the data
df.tail(4)

#フィーチャデータセットを作成して印刷します。
X = np.array(df.drop(['Prediction'],1))[:-future_days] 
print(X)

#ターゲットデータセットを作成して印刷します。
y = np.array(df ['Prediction'])[:-future_days] 
print(y)


#データを75％のトレーニングデータセットと25％のテストデータセットに分割します。
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size = 0.25)


# モデルを作成する時間です。
# このプログラムで使用されるモデルは、ディシジョンツリーリグレッサと線形回帰を使用します。
# デシジョンツリーリグレッサモデル
tree = DecisionTreeRegressor().fit(x_train, y_train)
# 線形回帰モデルを作成する
lr = LinearRegression().fit(x_train, y_train)



#機能データセットから最後の「x」行を取得して印刷します。
# このデータセットを使用してモデルをテストし、モデルのパフォーマンスを確認します。
#特徴データを取得します。
#AKA最後の 'x'日を除く元のデータセットのすべての行
x_future = df.drop(['Prediction'],1)[:-future_days] 
#最後の 'x'行を取得します
x_future = x_future.tail(future_days)
#データセットをnumpy配列に
x_future = np.array(x_future)
x_future



#モデルの予測を表示します。
#モデルツリー予測を
tree_prediction = tree.predict(x_future)
print( tree_prediction )
print()
#モデル線形回帰予測を
lr_prediction = lr.predict(x_future)
print(lr_prediction)


#予測値を視覚化し、実際の値または有効な値と比較します。
#データ予測の視覚
predictions = tree_prediction
#データのプロット
valid =  df[X.shape[0]:]
valid['Predictions'] = predictions #予測価格を保持する「Predictions」という新しい列を作成する
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.plot(df['Adj Close'])
plt.plot(valid[['Adj Close','Predictions']])
plt.legend(['Train', 'Val', 'Prediction' ], loc='lower right')
plt.show()


#Visualize the data
predictions = lr_prediction
#Plot the data
valid =  df[X.shape[0]:]
valid['Predictions'] = predictions #Create a new column called 'Predictions' that will hold the predicted prices
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.plot(df['Adj Close'])
plt.plot(valid[['Adj Close','Predictions']])
plt.legend(['Train', 'Val', 'Prediction' ], loc='lower right')
plt.show()

#このように予測値と実際の結果が出力されたことが確認できます。
# 青色が機械学習を行った実際の過去のデータです。
# 黄色が機械学習によって予測されたデータです。
# 赤色がその時の実際の株価データです。
# はい、今回はSONY社の過去の株価データからLSTMを用いて株価分析まで行ってみました。
# 初心者の方には凄く難しい内容になったと反省しております。また再度わかりやすい講座にリメイクさせていただきます。