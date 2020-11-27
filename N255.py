#Deep Learning ディープラーニングで株価予想



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

#次に、2014年から今日までの6年間のデータを取得しましょう。期日を決めて行きます。
start_date="2020-01-01"

#終了日はプログラムの実行日にしたいので、日時と文字列を相互に変換するメソッドstrftime関数を使います。様々なフォーマットの日付や時間を操作することが可能です。
end_date= datetime.today().strftime("%Y-%m-%d")

#次に必要のないデータをカットして行きましょう。今回は終わり値だけ分析を行います。
#data = web.DataReader('SNE',data_source ="yahoo",start = start_date,end = end_date)["Adj Close"]
data = web.DataReader("SNE",data_source="yahoo",start=start_date,end=end_date)

# 次にデータを加工するため新しい変数にデータを入れ込みます。
sony_data = data.filter(["Close"])

data = sony_data
#google_dataの各要素をgoogle_close変数に入れ込みます。
sony_close = sony_data.values

plt.figure(figsize=(16,8))
plt.plot(data)

plt.show()

model_1 = Sequential()
model_1.add(Dense(5, activation='relu', input_shape=(20,)))
model_1.add(Dropout(0.5))
model_1.add(Dense(1, activation='linear'))
model_1.summary()
model_1.compile(optimizer='adam',loss='mse',metrics=['mae'])



model_2 = Sequential()
model_2.add(LSTM(10,
             dropout=0.2,
             recurrent_dropout=0.2,
             input_shape=(20,1)))
model_2.add(Dense(5, activation='relu'))
model_2.add(Dropout(0.5))
model_2.add(Dense(1, activation='sigmoid'))
model_2.summary()
model_2.compile(optimizer='adam',
           loss='binary_crossentropy',
           metrics=['acc'])



# 出力ラベルを、次の日Topixの値が上がったら「１」、
# 1次の日Topixの値が下がったら「０」とする関数は、以下のようになります。
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


#model_1予測
predicted = model_1.predict(X_test)

result = pd.DataFrame(predicted)

result.columns = ['predict']
result['actual'] = y_test
plt.figure(figsize=(16,8))
plt.plot(result)
plt.show()



#mdel_2予測
predicted = model_2.predict(X_test[:,:,np.newaxis])
result = pd.DataFrame(predicted)
result.columns = ['predict']
result['actual'] = y_test
plt.figure(figsize=(16,8))
plt.plot(result)
plt.show()



def updown(actual, predict):
 act = np.sign(np.diff(actual))
 pre = np.sign(np.diff(predict[:,0]))
 tmp =  act*pre>0
 return np.sum(tmp)/len(tmp)


print('model_1:',updown(y_test, model_1.predict(X_test)))
print('model_2:',updown(y_test, model_2.predict(X_test[:,:,np.newaxis])))


#テストデータの正解率を見てみましょう。
print(model_2.evaluate(X_test[:,:,np.newaxis], y_test))

