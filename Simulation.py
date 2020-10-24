# 必要なライブラリをimportします
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# 可視化のためのセットです。
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
#%matplotlib inline

# Yahooからデータを読み込めるようにします
from pandas_datareader import DataReader

# Pythonで日付と時刻を扱うためのモジュールです
from datetime import datetime

# Python2を使っている場合は必要です
#from __future__ import division



# 所謂ハイテク企業の株価を扱ってみます。
tech_list = ['AAPL','GOOG','MSFT','AMZN']
tech_list1 = ['stock_N225.csv']
# 直近1年間のデータを使ってみましょう。
end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)

# それぞれの企業ごとに、Yahooのサイトからデータを取得します

# csv ファイルからの時系列データ読み込み
filename = tech_list1 # 日経平均株価データ


for stock in tech_list1:   
    # それぞれの名前でDataFrameを作ります。
    #globals()[stock] = DataReader(stock, 'yahoo', start, end)
    globals()[stock] = pd.read_csv(stock, index_col=0, parse_dates=True)
    
# データの概観を掴むことができます。
AAPL.describe()
AAPL.info()

# 終値の時系列をプロットしてみます。
AAPL['Adj Close'].plot(legend=True, figsize=(10, 4))
plt.show()



# 今度は出来高（1日に取引が成立した株の数）をプロットします。
AAPL['Volume'].plot(legend=True,figsize=(10,4))
plt.show()


# pandasはもともと金融情報を扱うために作られていたので、色々な機能があります。

# 間隔ごとに移動平均を描いてみます。
ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA {}".format(str(ma))
    AAPL[column_name] = AAPL['Adj Close'].rolling(ma).mean()

AAPL[['Adj Close', 'MA 10', 'MA 20', 'MA 50']].plot(subplots=False, figsize=(10, 4))
plt.show()


#株式投資のリスクを管理するために、日ごとの変動について計算してみます。
# pct_changeを使うと、変化の割合を計算できます。
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
# 変化率をプロットしてみましょう。
AAPL['Daily Return'].plot(figsize=(10, 4), legend=True, linestyle='--', marker='o')
plt.show()



#前日比（％）のヒストグラムを描いてみましょう。Seabornを使えば、KDEプロットも一緒に描けます。
# NaNを取り除くコードを書いておく必要があります。
sns.distplot(AAPL['Daily Return'].dropna(), bins=100, color='purple')
# こんなコードでもOK
# AAPL['Daily Return'].hist(bins=100)



#ハイテク4社の株価を1つのDataFrameにまとめてみましょう。
# 簡単なコードで実現出来ます。
closing_df = DataReader(['AAPL','GOOG','MSFT','AMZN'],'yahoo',start,end)['Adj Close']

# 確認しておきましょう。
closing_df.head()
plt.show()

#アップル社でやったように、終値の日ごとの変化を計算します。
# 別のDataFrameにしておきます。
tech_rets = closing_df.pct_change()
#終値の変化を会社ごとに比較できるようになりました。
# Google同士なら、完全に相関します。
sns.jointplot('GOOG', 'GOOG', tech_rets, kind='scatter', color='seagreen')
plt.show()

#相関があるかどうか、別の会社同士を比べてみましょう。
# GoogleとMicrosoftを比べてみます。
sns.jointplot('GOOG', 'MSFT', tech_rets, kind='scatter')
plt.show()


