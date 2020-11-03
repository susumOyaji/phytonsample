'''
第１回 python finance1

今回は大手IT企業GAFAの過去の株価データより株価分析を行います。知らない方のためにGAFAとはGoogle、Amazon、Facebook、Appleという大手IT企業の頭文字をとったものです。早速、GAFAの株価を取得してみましょう٩( ‘ω’ )و

まずはライブラリーをimport していきましょう。

日付・時刻ライブラリーをインポートします。いつからいつまでの株価を取得するかを決めるためインポートします。

from datetime import datetime
次に株価を取得するためpandas_datareaderをimport します。pandas_datareaderはweb上の様々なソースに簡単にアクセスして、株価や為替レート、人口などのデータを取得できるものです。

import pandas_datareader as web
次に取得したデータをグラフ化させる。matplotlibをインポートします。

import matplotlib.pyplot as plt
次にここからが重要です。ここで株式シンボルを取得します。その後に、株式情報の取得日（開始日と終了日）を決めます。そして、取得したデータからグラフを作成し、単純な株式で得れるリターン(利益)を毎日計算してみましょう٩( ‘ω’ )و

今回はGAFAのシンボルを取得してみます。つまり、Google Amazon Facebook Apple の株価を取得します。ティッカーシンボル変数に代入していきます。

Googleは“GOOG”、Amazonは“AMZN”、Facebookは“FB”、Appleは“AAPL”と記載します。このように書きます

ticker_symbols=[ “GOOG” , “AMZN” , “FB” , “AAPL” ]
皆さんが他に表示したい株があった場合。例えば、ソニー株を表示したい場合は「ソニー ティッカーシンボル」と検索すればすぐに確認できます。ちなみに、ソニーの場合はSNEで、ソフトバンクの場合はSFTBYと記載すれば取得できます。

次に取得日の開始日と終了日を設定しましょう。今回は2014年から本日までの6年間を取得したいと思います。

startdate=’2014-01-01’
終了日は実行時の日にしたいので、日時と文字列を相互に変換するメソッドstrftime関数を使います。様々なフォーマットの日付や時間を操作することが可能です。

today = datetime.today().strftime(‘%Y-%m-%d’)
実際に確認してみましょう。

print(today)
このように、本日のデータを取得できます。

では次に株価のデータを取得する関数を作成しましょう。d(￣ ￣)

引数にはもちろん作ったticker_symbols、と取得期間を記載しましょう。今回は終値だけ取得してみたいと思います。ですので、カラムを終値と記載します。

def getMyStock(stock=ticker_symbols , start = startdate , end = today , col=‘Adj Close’):
次にdata変数にヤフーから持ってきたGAFAの株価のデータを入れます。終値だけ欲しいので指定してあげます。

data=web,DataReader(stock , data_source=‘yahoo’ , start=start , end = end )[col]
取得したデータを関数の呼び出し元に返すようにしましょう。

return data
それでは実際にこの関数を呼び出して、表示してみます。

my_stock = getMyStock()
print(my_stock)
これを実行してみますと。このように終値の値が営業日のみ取得できていることが確認できます。データだと少しわかりにくいですので、グラフにしてみましょう。

①グラフにする関数を作成します。

def  graph_plot(stocks=ticker_symbols , start = startdate , end = today , col=‘Adj Close’)
グラフのタイトルを決めます。

title= col + ‘Price History’
そして、先ほどと同様に、関数を呼び出しDataReaderから株価のデータを取得します。

my_stocks = getMyStock(stocks=stocks , start = start , end = end , col=col)
次にマットプロットライブを使ってグラフ化させましょう。図のサイズを決めます。今回は幅は18 高さは8にします。

plt.figure(figsize=(18,8))
次にデータを全てプロットさせて行きます。

for i in my_stocks.columns.values:
        plt.plot(my_stocks[i],label = i)
次にグラフにタイトルを入れ込みます。

plt.title(title)
次にグラフのｘ軸のラベルの名前を記載します。今回の場合はGAFA_dataと記載します。

plt.xlabel("GAFA_date",fontsize=16)
次にグラフのy 軸のラベルの名前を記載します。今回の場合はAdj Close Price ($)と記載します。

plt.ylabel(col+"Price ($)",fontsize=16)
次に、アンカーを左上におきます。

plt.legend(my_stocks.columns.values,loc= "upper left")
アンカーを右下に置きたい場合lower rightと記載すればできます。グラフを表示します。

plt.show()
実際にこの関数を呼び出してみましょう。

graph_plot(ticker_symbols)
これで実行してみますと。

このようにGAFAのデータをグラフ化することができたことが確認できます。x軸にはタイトルもy軸にもタイトルが付いていることが確認できます。また左上にアンカーがあることも確認できます。ちなみに私は2016年の時期にAMAZONの株を保有しておりましたが、その翌年にかけて急激に下がってしまったので売却してしまいました。このグラフを確認しますと保有しておけばと思います。(T . T)

はい、今回は大手IT企業GAFAの過去の株価データからグラフを表示してみました。

ティッカーシンボルから表示したい株を特定し、マットプロットライブを使ってグラフ化まで行いました。

次回のpython finance2では実際の株式運用を想定した、他の株価との相関関係の調べ方やリターンの計算方法や共分散行列やボラリティなどから実際的な運用方法の解説まで行っております。LSTMを用いたAiで実際に株価の予測はpython finance3で行っています。具体的にはグーグル社の株価の予測と実際株価結果の確認まで行っています。是非興味がある方はご覧ください。

以上で、python finance1を終了致します。ご清聴ありがとうございました(๑╹ω╹๑ )
'''


from datetime import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt

stockSymbols=[ "SNE" , "AAPL" , "TYOYY" , "RKUNY" ]

stockStartDate="2020-01-01"

today = datetime.today().strftime("%Y-%m-%d")

def getMyPortfolio(stocks=stockSymbols , start = stockStartDate , end = today , col="Adj Close"):
    data = web.DataReader(stocks , data_source="yahoo", start=start , end = end )[col]
    return data
    
def showGraph(stocks=stockSymbols , start = stockStartDate , end = today , col="Adj Close"):
    
    title= "Portfolio"+ col + "Price History"
    my_stocks = getMyPortfolio(stocks=stocks , start = start , end = end , col=col)
    
    plt.figure(figsize=(18,8))
    
    for c in my_stocks.columns.values:
        plt.plot(my_stocks[c] , label = c)
        
    plt.title(title)
    plt.xlabel("Date" , fontsize=18)
    plt.ylabel(col+"Price USD ($)", fontsize=18 )
    
    plt.legend(my_stocks.columns.values , loc="upper left")
    
    plt.show()

    
showGraph(stockSymbols)