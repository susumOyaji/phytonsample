import sqlite3
import pickle
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.layers import Input, Dense, LSTM
from keras.models import Model
from keras.callbacks import CSVLogger
from sklearn.preprocessing import StandardScaler
#pandasのdatareaderをwebとしてインポートします。
import pandas_datareader as web
from datetime import datetime






today = datetime.today().strftime("%Y-%m-%d")
#次に、期日を決めて行きます。
start_date="2020-01-01"

#終了日はプログラムの実行日にしたいので、日時と文字列を相互に変換するメソッドstrftime関数を使います。様々なフォーマットの日付や時間を操作することが可能です。
end_date = datetime.today().strftime("%Y-%m-%d")


# データを読み込む
df = web.DataReader("RKUNY",data_source="yahoo",start=start_date,end=end_date)
#print(df)

# 終値だけを取り出す
closes = df['Adj Close'].values
base_data = closes.reshape(-1,1)

# データの前処理と正規化
# テストデータと訓練データへ分割
# 今回は訓練データを全体の8割、テストデータを残り2割としています。 また、データの標準化も行います
# 全データのうち、80% を学習用データ、20% を検証用データに割り当て

# 特徴量の尺度を揃える：特徴データを標準化して配列に入れる
scaler = StandardScaler()


# 特徴データを標準化（平均0、分散1になるように変換）
data = scaler.fit_transform(base_data)
x_data = []
y_data_price = []
y_data_updown = []


# 10 日分の日経平均株価を入力として、1 日後の日経平均株価を予測
for i in range(len(data) - 10):
    x_data.append(data[i:i + 10])
    y_data_price.append(data[i + 10])
    y_data_updown.append(int((base_data[i + 10 - 1] - base_data[i + 10]) > 0))
x_data = np.asarray(x_data).reshape((-1, 10, 1))
y_data_price = np.asarray(y_data_price)
y_data_updown = np.asarray(y_data_updown)

# 学習データサイズ
train_size = int(len(data) * 0.8)

# 学習データ
x_train = x_data[:train_size]
y_train_price = y_data_price[:train_size]
y_train_updown = y_data_updown[:train_size]

# テストデータ
x_test = x_data[train_size:]
y_test_price = y_data_price[train_size:]
y_test_updown = y_data_updown[train_size:]
#今回のネットワークはごく単純な LSTM とし、Keras を使って組んでいきます。

#Long Short Term Memory ネットワークは、通常は「LSTM」と呼ばれ、長期的な依存関係を学習することのできる、RNNの特別な一種です。 

#LSTMネットワークの概要

# LSTM を Keras を使って組む
inputs = Input(shape=(10, 1))

# 日経平均株価の値を直接予測するため活性化関数は linear
# 中間層の数は 32（理由なし）
x = LSTM(32, activation='relu')(inputs)
price = Dense(1, activation='linear', name='price')(x)
updown = Dense(1, activation='sigmoid', name='updown')(x)
model = Model(inputs=inputs, outputs=[price, updown])

# 後で検証に使用するため 2 値予測も含んでいる
model.compile(loss={
    'price': 'mape',
    'updown': 'binary_crossentropy',
}, optimizer='adam', metrics={'updown': 'accuracy'})

#エポックは 100、バッチサイズは 10
model.fit(x_train, [y_train_price, y_train_updown],
          validation_data=(x_test, [y_test_price, y_test_updown]), epochs=1000, batch_size=10, verbose=0)
          #callbacks=[CSVLogger('train.log.csv')])
# モデルのsave/load
model.save('model.h5')


#誤差が下がっていってますので、正常に学習できているようです。
 
#確認
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f, protocol=pickle.HIGHEST_PROTOCOL)
pred = model.predict(x_test)[0][:, 0].reshape(-1)
#-----------------------------------------------------------------------------------------------

# 標準化を戻す
pred = scaler.inverse_transform(pred)
y_test_price = scaler.inverse_transform(y_test_price)


#学習したモデルで予測した日経平均株価のグラフを書く
# plot準備
result = pd.DataFrame({'pred': pred, 'test': y_test_price.reshape(-1,)})
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
result.plot()
plt.show()
