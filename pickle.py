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
'''
def read_data():
    paths = Path('.').glob('./indices_I101_1d_*.csv')
    df = pd.concat([pd.read_csv(p, index_col='日付', parse_dates=True, encoding='cp932')
                    for p in paths])
    df = df.sort_index()
    closes = df['終値'].values
    return closes
'''
today = datetime.today().strftime("%Y-%m-%d")

#次に、2014年から今日までの6年間のデータを取得しましょう。期日を決めて行きます。
start_date="2020-01-01"

#終了日はプログラムの実行日にしたいので、日時と文字列を相互に変換するメソッドstrftime関数を使います。様々なフォーマットの日付や時間を操作することが可能です。
end_date = datetime.today().strftime("%Y-%m-%d")




# ディープラーニングで株価予測
# モデルは 10 日分の平均株価を入力として、1 日後の平均株価を予測することとします。
# ですので、取得したデータを読み込んで日付順にソートした後、終値だけを取り出します。
def read_data():
    '''
    df = pd.read_csv(r'stock_N225.csv',
               	encoding='shift_jis',
              	index_col='Date',
               	parse_dates=True,
                dtype='float64').dropna(axis=1).dropna()
    '''
    df = web.DataReader("RKUNY",data_source="yahoo",start=start_date,end=end_date)
    df = df.sort_index()
    closes = df['Adj Close'].values
    base_data = closes.reshape(-1,1)
    print(base_data)
    return closes


#今回のネットワークはごく単純な LSTM とし、Keras を使って組んでいきます。
def create_model():
    inputs = Input(shape=(10, 1))
    x = LSTM(300, activation='relu')(inputs)
    price = Dense(1, activation='linear', name='price')(x)
    updown = Dense(1, activation='sigmoid', name='updown')(x)
    model = Model(inputs=inputs, outputs=[price, updown])
    model.compile(loss={
        'price': 'mape',
        'updown': 'binary_crossentropy',
    }, optimizer='adam', metrics={'updown': 'accuracy'})
    return model





# 平均株価の値を直接予測するため活性化関数は linear を使います。中間層の数は 300 としていますが特に理由はありません。
# 後で検証に使用するため 2 値予測も含んでいます。
# 全データのうち、80% を学習用データ、20% を検証用データに割り当てます。また、データの標準化も行います。
def build_train_test_data(base_data):
    scaler = StandardScaler()
    data = scaler.fit_transform(base_data)
    #data = base_data
    x_data = []
    y_data_price = []
    y_data_updown = []
    for i in range(len(data) - 10):
        x_data.append(data[i:i + 10])
        y_data_price.append(data[i + 10])
        y_data_updown.append(int((base_data[i + 10 - 1] - base_data[i + 10]) > 0))
    x_data = np.asarray(x_data).reshape((-1, 10, 1))
    y_data_price = np.asarray(y_data_price)
    y_data_updown = np.asarray(y_data_updown)
    train_size = int(len(data) * 0.8)
    x_train = x_data[:train_size]
    y_train_price = y_data_price[:train_size]
    y_train_updown = y_data_updown[:train_size]
    x_test = x_data[train_size:]
    y_test_price = y_data_price[train_size:]
    y_test_updown = y_data_updown[train_size:]
    return x_train, y_train_price, y_train_updown, x_test, y_test_price, y_test_updown, scaler



#では学習していきます。エポックは 100、バッチサイズは 10 としていますが、これらも特に理由はありません。
def main():
    model = create_model()
    data = read_data()
    x_train, y_train_price, y_train_updown, x_test, y_test_price, y_test_updown, scaler =  \
        build_train_test_data(data)
        
    model.fit(x_train, [y_train_price, y_train_updown],
              validation_data=(x_test, [y_test_price, y_test_updown]), epochs=10, batch_size=10,
              callbacks=[CSVLogger('train.log.csv')])
    model.save('model.h5')



    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f, protocol=pickle.HIGHEST_PROTOCOL)
    pred = model.predict(x_test)[0][:, 0].reshape(-1)    

    # 標準化を戻す
    pred = scaler.inverse_transform(pred)
    #pred = scaler.inverse_transform(pred)
    y_test_price = scaler.inverse_transform(y_test_price.astype('float64'))


    #学習したモデルで予測した日経平均株価のグラフを書く
    # plot準備
    result = pd.DataFrame({'pred': pred, 'test': y_test_price})
    result.plot()
    plt.show()


if __name__ == '__main__':
    main()