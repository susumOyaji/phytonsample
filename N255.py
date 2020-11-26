
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from keras.layers import Dense, LSTM, Dropout, Flatten
from keras.models import Model
#層を積み上げるためkerasからSequentialのインポートします。
from keras.models import Sequential
from datetime import datetime
#pandasのdatareaderをwebとしてインポートします。
import pandas_datareader as web




data = pd.read_csv(r'stock_N225.csv',
               	encoding='shift_jis',
              	index_col='Date',
               	parse_dates=True,
               	dtype='float64').dropna(axis = 1).dropna()

today = datetime.today().strftime("%Y-%m-%d")
data = web.DataReader("GOOG",data_source="yahoo",start="2012-01-01",end="2020-06-01")

# 次にデータを加工するため新しい変数にデータを入れ込みます。
sony_data = data.filter(["Close"])

#google_dataの各要素をgoogle_close変数に入れ込みます。
sony_close = sony_data.values

data.plot()
plt.show()

model_1 = Sequential()
model_1.add(Dense(5, activation='relu', input_shape=(20,)))
model_1.add(Dropout(0.5))
model_1.add(Dense(1, activation='linear'))
model_1.summary()
model_1.compile(optimizer='adam',loss='mse',metrics=['mae'])



model_2 = Sequential()
model_2.add(LSTM(10,dropout=0.2,recurrent_dropout=0.2,input_shape=(20,1)))
model_2.add(Dense(5, activation='relu'))
model_2.add(Dropout(0.5))
model_2.add(Dense(1, activation='linear'))
model_2.summary()
model_2.compile(optimizer='adam',loss='mse',metrics=['mae'])





def getInputLabel(data, period=20):
 period = period
 input_tensor = []
 label_tensor = []
 for i in range(0, len(data) - period, 1):
     input_tensor.append(data.values[i:i + period, 0])
     label_tensor.append(np.diff(data.values[:,0])[i + period -1])
 input_tensor = np.array(input_tensor)
 label_tensor = np.sign(np.array(label_tensor))
 label_tensor[label_tensor<0] = 0
 return input_tensor, label_tensor


tmp = data - data.mean()
tmp = tmp/data.std()
input_tensor, label_tensor = getInputLabel(data = tmp)




# 機械学習の分野では、「トレーニングデータでパラメータの学習」を行い、
# 「テストデータを用いて そのパラメータの評価」を行います。
# トレーニングデータとテストデータに分割
# test_size=0.2 と指定することでデータを、8:2でトレーニングデータとテストデータに分割しました。
X_train, X_test, y_train, y_test = train_test_split(input_tensor, label_tensor, test_size=0.2,random_state=100, shuffle = False)


#ディープラーニング実践
#モデルの過学習を防ぐために、以下のようにコールバックを設定しましょう。
earlystopping = EarlyStopping(monitor='loss', patience=5)

model_1.fit(X_train, y_train, batch_size=10, epochs=50, callbacks=[earlystopping])
model_2.fit(X_train[:,:,np.newaxis], y_train, batch_size=10, epochs=50, callbacks=[earlystopping])

predicted = model_1.predict(X_test)
result = pd.DataFrame(predicted)
result.columns = ['predict']
result['actual'] = y_test
result.plot()
plt.show()

predicted = model_2.predict(X_test[:,:,np.newaxis])
result = pd.DataFrame(predicted)
result.columns = ['predict']
result['actual'] = y_test
result.plot()
plt.show()






#テストデータの正解率を見てみましょう。
model_2.evaluate(X_test[:,:,np.newaxis], y_test)

