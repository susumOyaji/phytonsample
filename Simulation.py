# 必要なライブラリをimportします
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from bs4 import BeautifulSoup
import requests
import csv

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
tech_list = ['998407','AAPL','GOOG','MSFT','AMZN']
tech_list1 = ['stock_N225.csv']
# 直近1年間のデータを使ってみましょう。
end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)

# それぞれの企業ごとに、Yahooのサイトからデータを取得します
#url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6758"  #^DJI
#    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#    print(soup)

urlName1 ='https://info.finance.yahoo.co.jp/ranking/?kd=29&mk=3&tm=d&vl=a'#年初来高値
soup1 = BeautifulSoup(requests.get(urlName1).content, 'html.parser')
text1 = soup1.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
data1 = [d.text for d in soup1.find_all('td')]
data_1 = np.array(data1).reshape(int(len(data1) / 9), 9).tolist()
df1 = pd.DataFrame(data = data_1)
df1.columns = ["code","market","name","Trading time","Transaction price","business day","Year-to-date high","High price","Bulletin board"]  #カラム名を付ける
#df1.columns = ["ｺｰﾄﾞ","市場","名称","取引時間","取引値","前営業","年初来高値","高値","掲示板"]  #カラム名を付ける
#data2.index   = [11,12,13,14,15,16]  #インデックス名を付ける


urlName2 = 'https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=3&tm=d&vl=a'#値上がり率
soup2 = BeautifulSoup(requests.get(urlName2).content, 'html.parser')
text2 = soup2.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
data2 = [d.text for d in soup2.find_all('td')]

urlName3 ='https://info.finance.yahoo.co.jp/ranking/?kd=32&mk=3&tm=d&vl=a'#単元当たり出来高  
soup3 = BeautifulSoup(requests.get(urlName3).content, 'html.parser')
text3 = soup3.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
data3 = [d.text for d in soup3.find_all('td')]


urlName4 = 'https://info.finance.yahoo.co.jp/ranking/?kd=27&mk=3&tm=d&vl=a'#ストップ高  
soup4 = BeautifulSoup(requests.get(urlName4).content, 'html.parser')
text4 = soup4.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
data4 = [d.text for d in soup4.find_all('td')]





  
#data1 = [d.text for d in soup1.find_all('td')]
#data2 = np.array(data1).reshape(int(len(data1) / 9), 9).tolist()
#df = pd.DataFrame(data = data2)
#df.columns = ["ｺｰﾄﾞ","市場","名称","today","stock","day","stock1","stock2","a"]  #カラム名を付ける
#data2.index   = [11,12,13,14,15,16]  #インデックス名を付ける

print(list(df1.columns))
print(df1.values)

#データをいじってみよう
#データから特定の列だけを選択する
#組み込み関数__get_item___を使った選択
df1["code"] #列名を書いて指定
select = df1[["code","market","name","High price"]] #複数列を選択する場合にはリスト表記を使う
print(select)



df1.to_csv('CSVファイル名.csv')
data = pd.read_csv('CSVファイル名.csv',index_col=0)
data.plot(legend=True, figsize=(10, 4))
#plt.show()


#data.plot(x=data["ｺｰﾄﾞ"],y=data["stock2"], kind='hist', bins=15)
#plt.show()





# csv ファイルからの時系列データ読み込み
#filename = 'N225.csv' # 日経平均株価データ
#filename = tech_list # 日経平均株価データ

#data = pd.read_csv(df)

#for stock in tech_list1:   
    # それぞれの名前でDataFrameを作ります。
    #globals()[stock] = DataReader(stock, 'yahoo', start, end)
    #globals()[stock] = pd.read_csv(filename, index_col=0, parse_dates=True)
    
# データの概観を掴むことができます。
#AAPL.describe()
#AAPL.info()
#df.describe()
#df.info()

# 終値の時系列をプロットしてみます。
data['code'].plot(legend=True, figsize=(10, 3))
#plt.show()



# 今度は出来高（1日に取引が成立した株の数）をプロットします。
data['code'].plot(legend=True,figsize=(10,4))
#plt.show()


# pandasはもともと金融情報を扱うために作られていたので、色々な機能があります。

# 間隔ごとに移動平均を描いてみます。
ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA {}".format(str(ma))
    data[column_name] = data['code'].rolling(ma).mean()

data[['code', 'MA 10', 'MA 20', 'MA 50']].plot(subplots=False, figsize=(10, 4))
#plt.show()


#株式投資のリスクを管理するために、日ごとの変動について計算してみます。
# pct_changeを使うと、変化の割合を計算できます。
_data = []
for rep in range(5):
    print(type(data['High price'][rep]))
    _data = float(data['High price'][rep].replace(',',''))
    print(_data)

    


#print(float(data['High price']))
data['Daily Return'] = _data.pct_change()
# 変化率をプロットしてみましょう。
data['Daily Return'].plot(figsize=(10, 4), legend=True, linestyle='--', marker='o')
plt.show()



#前日比（％）のヒストグラムを描いてみましょう。Seabornを使えば、KDEプロットも一緒に描けます。
# NaNを取り除くコードを書いておく必要があります。
sns.distplot(data['Daily Return'].dropna(), bins=100, color='purple')
# こんなコードでもOK
# AAPL['Daily Return'].hist(bins=100)






'''
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
'''

