'''
前回はGAFAの株価をグラフ化させ、表示させるところまで、出来ましたよね。今回は、実際に株式資産運用を想定した、株の相関関係の調べ方やリターンの計算方法、共分散やボラリティなどから株式資産運用方法の解説まで行っていきます。はい、今回もpythonを使ってanacondaのspyderで解説致します。

まず、何からするかと言いますと、GAFAの株価データから、１日あたりの変化率を確認してみましょう。変化率を簡単に取得できるpct_change関数を使用します。pct_changeとは、新しい価格を古い価格で割って変化率を確認するという機能関数です。graph_plot関数内に入れ込んで確認してみます。

このように記載しします。

daily_rate_change = my_stocks.pct_change(1)
実際に変化率を表示してみましょう。

    print(daily_rate_change)
これで実行してみましょう。

このように変化率が確認できます。計算の仕組みは今回の場合は、今日の値、割る、前日の値、に引く１をします。変動がなければ当然割った値が１になりますので、結果は0になります。変動がプラスであった場合は、分子が大きくなりますので、割った値が１より大きくなります。そのため、１を引いても変動率はプラスなります。反対に変動がマイナスだった場合は、分母が小さくなり１より小さくなりますので、結果として変動率はマイナスが残ります。このデータから１日毎の変動の大きさを確認できます。

次に、GAFAの相関関係を確認してみましょう。投資家の方はよくご存知だと思いますが、株価の変動にはある程度の相関関係が確認できます。例えば原油の価格が上がれば、相対的にガゾリン会社やカナダドルという通貨に、影響があると言われております。他にも、大手企業の業績が悪化した場合は、連動する会社、つまり下請けの会社などの業績も影響があると言われております。

相関関係を調べる際はIT企業とIT企業ではなく、物流企業と飲食企業など、更には飲食企業のどの企業が国内または国外でどのくらいシェアを占めているのか、それを確認したのうえで相関関係を調べます。ここまでしか公表できませんが、要は絞りに絞ることで株価の予測がしやすく旨味のみ取得することができます。

実際にどのように調べるかと言いますと、簡単でcorr関数を使います。

このように記載します。

print(daily_rate_change.corr())
これで実行してみます。

このように相関関係が確認できます。簡単に説明しますと、ある１つの株価上昇中に他の株価下落している場合はマイナスになります。このデータだけを見ると、AmazonとGoogleは景気の動向が同じ、というようなことが確認できます。

※悪までこのデータのみから読み取れるものです。

次に、共分散を確認してみましょう。共分散というのは簡単に言いますと、2組の対応するデータが、どれほどお互いに影響を持ちながら散らばっているかを表します。つまりは、株の配当を目的とした投資家に該当する内容となりますね。実際にどのように調べるかと言いますと

簡単でcov関数を使います。

このように記載します。

print(daily_rate_change.cov())
これで実行してみます。

このように共分散行列が確認できます。要は、分散の値が高いということは、資産リスクが高いと覚えておいてください。※1つ注意点として、共分散行列で確認できるのはアンシステマティック・リスク(非市場リスク)と呼ばれている銘柄固有の要因によるリスクであることです。経済や社会情勢等のマクロ的要因であるシステマティック・リスク(市場リスク)が発生した場合は、リスク低減効果が通用ません。例えば、コロナウイルス期間の株価データによる相関関係は通用しないというイメージです。コロナウイルスによってそもそも経済自体が稼働していないためです。ちなみに、東京証券取引の１部上場企業の全データの相関関係を調べたい場合は、膨大な数になることから共分散行列使って相関関係を一気に絞り込むこともできます。

次に株価のボラティリティーの平均をだしていきます。つまり、標準偏差を計算するstd関数を使います。このように記載します。

print(daily_rate_change.std())
これを実行しますと、

どの企業がボラティリティーが高いか確認できます。このデータだけを見ると、Googleに投資するよりもFacebookに投資した方がリターンは大きいことが確認できます。

※悪まで個人の見解です。

次にボラリティを視覚化させましょう。

●上のグラフは消しましょう。

matplotlibを使ってグラフ化させましょう。図のサイズを決めます。今回は幅は18 高さは8にします。

plt.figure(figsize=(18,8))
次にデータを全てプロットさせて行きます。

for i in daily_rate_change.columns.values:
        plt.plot(daily_rate_change.index,daily_rate_change[I],lw=2,label=i)
次にグラフにタイトルを入れ込みます

plt.title(“Volatillity”)
次にグラフのｘ軸のラベルの名前を記載します。今回の場合はGAFA_dataと記載します。

plt.xlabel("GAFA_date",fontsize=16)
次にグラフのy 軸のラベルの名前を記載します。今回の場合はDaily_Volatillityと記載します。

plt.ylabel("Daily_Volatillity")
次に、アンカーを設定します。今回は右上

plt.legend(loc="upper right" , fontsize=10)
グラフを表示します。

plt.show()
これで実行してみましょう。

このようにデータが出力することができたことが確認できます。このグラフを確認してみますと、ボラリティからはFacebookは非常に不安定であると確認できます。それに比べgoogleは揮発性がなく安定しているように見えます。このように視覚化することもできます。

次に毎日の平均を表示したいと思います。先ほどにmean関数を入れて、変数に打ち込みます。

daily_mean_returns= daily_rate_change.mean()
print(“Daily mean return:”)
print(daily_mean_returns)
次にお客様が実際に株式でポートフォリオを形成した場合にどのような利益ができるかの計算をしてみましょう。※投資を知らない方のために、投資は基本的には、１社のみに投資をすることはありません。１社が潰れてしまった場合、全資産を失う可能性があるためです。ですので、投資をする際は何社かに資産を分配し、資産運用を行います。

今回は仮にgoogle40%とamazon30%とFacebook20%とapple10%で資産運用した場合のリターンの計算を行います。

このように記載できます。

Portfolio_Proportion = np.array([0.4 , 0.3 , 0.2 , 0.1])
作った配列と先ほど出した結果をかけます。

daily_mean_portfolio = np.sum(daily_mean_returns*Portfolio_Proportion)
そして、キャストしてこの結果を表示しましょう。

print(str(daily_mean_portfolio))
実行結果を見てみますと

１0ポイント回収ができていることが確認できます。これはポートフォリオとしては悪くない結果だと思います。

はい、今回は大手IT企業GAFAの過去データから実際に株式資産運用を想定した、株の相関関係の調べ方やリターンの計算方法、共分散やボラリティなどから株式資産運用方法の解説まで行ってきました。次回のpython finance3では、LSTMを用いたAiの株価予測を行っていきます。具体的にはグーグル社の株価の予測と実際株価結果の確認まで行っていきます。是非興味がある方はご覧ください。

以上で、python finance2を終了致します。ご清聴ありがとうございました。(๑╹ω╹๑ )
'''


from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

ticker_symbols=[ "SNE" , "AAPL" , "TYOYY" , "RKUNY" ]
startdate="2014-01-01"
today = datetime.today().strftime("%Y-%m-%d")
print(today)

def getMyStock(stocks=ticker_symbols , start = startdate , end = today , col="Adj Close"):
    data = web.DataReader(stocks , data_source="yahoo", start=start , end = end )[col]
    return data
    
#my_stock = getMyStock()
#print(my_stock)

def graph_plot(stocks=ticker_symbols , start = startdate , end = today , col="Adj Close"):
    
    title= col + "Price History"
    my_stocks = getMyStock(stocks=stocks , start = start , end = end , col=col)
    daily_rate_change = my_stocks.pct_change(1)
    #print(daily_rate_change)
    #print(daily_rate_change.corr())
    #print(daily_rate_change.cov())
    #print(daily_rate_change.std())
    
    plt.figure(figsize=(18,8))
    for i in daily_rate_change.columns.values:
        plt.plot(daily_rate_change.index,daily_rate_change[i],lw=2,label=i)
    plt.title("Volatillity")
    plt.xlabel("GAFA_date" , fontsize=16)
    plt.ylabel("Daily Simple Returns")
    plt.legend(loc="upper right", fontsize=10)
    plt.show()
    daily_mean_returns= daily_rate_change.mean()
    print("Daily mean return:")
    print(daily_mean_returns)
    Portfolio_Proportion = np.array([0.4 , 0.3 , 0.2 , 0.1])
    daily_mean_portfolio = np.sum(daily_mean_returns*Portfolio_Proportion)
    print(str(daily_mean_portfolio))
graph_plot(ticker_symbols)