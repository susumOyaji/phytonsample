'''
python finance4
pythonで株価を分析し確認し予測してみよう
今回はコメントを頂きましたので、テクニカル分析の初歩であるゴールデンクロスと、デッドクロスを視覚化する方法についてご紹介します。
最後まで見てくださいましたら、移動平均の線がpythonで描けるようになり、テクニカル指標を視覚化する方法について解説を行って行きます。
また補足説明として投資における金融工学を少しご紹介します。是非最後までご覧ください。
行って欲しい講座などあれば、ツイッターのDMまでください。
何から始めるかといいますと、今回はマイクロソフト社の過去のデータを取ってきてみましょう。まず標準ライブライリーをインポートして行きます。日付・時刻ライブラリーをインポートします。いつからいつまでの株価を取得するかを決めるためインポートします。
'''

from datetime import datetime

#行列の計算をしやすくするためnumpyをインポートします。
import numpy as np

#データ加工をしやすくするためpandasをインポートします。
import pandas as pd

#株価のデータを取得するためpandas_datareaderをインポートします。
import pandas_datareader as web

#グラフ化するためにpylabをインポートします。※本体がmatplotlibでpylabはそのインターフェースだと思ってください。
from pylab import mpl,plt

#グラフのフォーマットを決めます。
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.style.use('seaborn')
plt.rcParams['font.family']='serif'

#次に、2014年から今日までの6年間のデータを取得しましょう。期日を決めて行きます。
start_date="2020-01-01"

#終了日はプログラムの実行日にしたいので、日時と文字列を相互に変換するメソッドstrftime関数を使います。様々なフォーマットの日付や時間を操作することが可能です。
end_date= datetime.today().strftime("%Y-%m-%d")

#今回はマイクロソフトの株で確認を行います。マイクロソフトのティッカーシンボルがMSFTです。
# 今回は2020年の1月1日から2020年の本日までの株式情報を取得して行きましょう。
sony_stock = web.DataReader('SNE',data_source ="yahoo",start = start_date,end = end_date)

#まずは取得できているか確認してみましょう。
print(sony_stock)

#使ってない標準ライブラリーをコメントアウトして実行してみます。
#これで実際にデータが取れていることが確認できます。

#次に必要のないデータをカットして行きましょう。今回は終わり値だけ分析を行います。
sony_stock_Adj_Close = web.DataReader('SNE',data_source ="yahoo",start = start_date,end = end_date)["Adj Close"]
#これを差し込んで実際に確認してみましょう。
#終わり値だけ取得できていることが確認できます。
print(sony_stock_Adj_Close)
#デッドクロスとゴールデンクロスを表示するという意味です。
'''
※投資を初心者の方のために、移動平均とは文字通り過去の履歴の平均値を表示しているものです。
投資の世界では単純移動平均を（SMA）と呼び、さらに短期SMAが長期SMAを上回る市場をゴーデンクロスと呼びます。
一般に投資家はロングポジションつまり（買い）を入れます。反対に長期SMAが短期SMAを上回る市場をデッドクロスと呼びます。
投資家はショートポジションつまり（売り）を入れます。
※ここで少しだけ注意喚起をします。
他にもダウ理論やグランビル法則、エリオット波動、ピボット手法など、たくさんの手法はありますが、株はそう簡単ではありません。
社会情勢によっても変動します。前回の動画でも少し触れましたが、テクニカル指標だけで稼ぐには統計学と金融工学を勉強する必要があります。
そもそも、どのようにして株の値動きが決まっているのか、インターバンクの仕組みはどのようになっているのか、それを把握する必要があります。
よく目にする投資家などの講演会では、そう言った情報は提供していません。
なぜなら彼らは投資で稼いでるのではなく、レベニューシェアや講演家として稼いでるからです。ですので皆さんのお金でご飯を食べている人が大半です。
私の知り合いに統計学と金融工学を駆使し、何億稼いだ成功者はいますがその人は一切情報を公開していません。人間はそういう生き物です。
ですので私たちも知識は提供しますが手法を伝授することは致しません。
人間はそうい生き物なのです。逆を言えば提供している人たちは案件であり皆さんのお金をとっているだけです。
オンラインサロンなんかも同じことです。現代版の一種の宗教団体が少しビジネスかじっただけです。
結局のところ成功するためには、自信の作品であり、製品であり、アプリなどを作りサービスを提供しないといけません。
'''
'''
list = microsoft_stock

#test = 'test'
#test_int = 111
data1 = {}


data1['STCK'] = microsoft_stock
data1['SMA1'] = microsoft_stock.rolling(window=25).mean()#list
data1['SMA2'] = microsoft_stock.rolling(window=50).mean()#list
print(data1['STCK'])
print(data1['SMA1'])
print(data1['SMA2'])

#data1['STCK'].plot(figsize=(18,8))
#data1['SMA1'].plot(figsize=(18,8))
#data1['SMA2'].plot(figsize=(18,8))
#print(data1)

data1['STCK', 'SMA1', 'SMA2'].plot(figsize=(18,8))

data1 = {}
data1[[microsoft_stock,'SMA1','SMA2']]
'''


# ②rollingを使って移動平均を計算します。ローリング統計を用いて単純移動平均を表示してみます。
# まずはマイクロソフトのデータを価格のみにしてあげましょう。
data={}
data_all = {}
# 次に短期SMAを設定します。(25期間の)
sony_stock['SMA1'] = sony_stock["Adj Close"].rolling(window=25).mean()#移動平均を求める際には、「rolling」と「mean」という関数を利用します。
print('SMA1',sony_stock)

sony_stock.query('SMA1 >= 5 | SMA1 <= -5').loc[:,['Data','Adj Close','SMA1','乖離率']]

'''
初めに、csvファイルをpandasに取り込みます。
>>> import pandas
>>> df = pandas.read_csv("./USDJPY.csv")

作成したデータフレームに、計算結果のカラムを新規で追加してあげます。右辺が計算式ですね。
>>> df['２５日移動平均'] = df['終値'].rolling(window=25).mean()
>>> df['乖離率'] = (df['終値'] - df['２５日移動平均']) / df['２５日移動平均'] * 100
'''


# カラムが追加されていることを確認できます。
# 25日以前は、必要なデータ数が不足しているので、NaN(Not a Number)となってます。


#次に長期SMAを設定します。(252期間の)
sony_stock['SMA2'] = sony_stock['Adj Close'].rolling(window=50).mean()
print('SMA2',sony_stock)



#図のタイトルを決めます。
plt.title("sony stock History")

#終値をプロットさせます。
#plt.plot(sony_stock["Adj Close"])

sony_stock['SMA1'].plot(figsize=(18, 8))
sony_stock['SMA2'].plot(figsize=(18, 8))


##############################################################################
#data_all = sony_stock_all#.groupby(pd.Grouper(level=0, freq='M')).mean()
#print('data_all',data_all)
#ax = data_all['High'].plot(legend=True)
#data_all[['Low', 'Open','Adj Close']].plot(ax=ax, rot=30)
plt.show()

#データをプロットして行きます。data(3要素のリストのリスト)
#df.plot()=df to displaydata(csv)

sony_stock[['Low','SMA1','SMA2']].plot(figsize=(18,8))

#③デッドクロスとゴールデンクロスを実際に可視化してみます。
#先ほどと同じように
#np.where(a < 4, True, False)条件を満たす場合はTrue, 満たさない場合はFalseとする。
sony_stock['positions'] = np.where(sony_stock['SMA1'] > sony_stock['SMA2'],1,-1)
#上記は三項演算ですね。

ax = sony_stock[[sony_stock,'SMA1','SMA2','positions']].plot(figsize=(10,6))
#ここで、アンカーも表示しましょう。

ax.get_legend().set_bbox_to_anchor((0.25,0.85))
#※ここで、注意点があります。データを取得した際にデータそのものに欠損がある場合があります。つまりNaNです。その時はdropna()関数で
dropna(inplace = True)

#で欠損のないデータが完成させることができます。簡単に説明しますと欠損しているデータを削除することができます。実際に確認してみましょう。
#④S&P500とVIXを表示したいと思います。S&P500で何ができるかと言いますと。まずは簡単にトレンドをグラフにしてみましょう。