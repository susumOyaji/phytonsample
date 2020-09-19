#必要なモジュールのインストール
from selenium import webdrive
import pandas as pd
import numpy as np
from plotlib import pyplot as plt
import matplotlib as inline #Google Chromeブラウザの表示
browser=webdriver.Chrome()#スクレイピングの準備
columnNames=[]
ETFComparisonsTable=[]
for num in range(0,50):




#リストから銘柄を選択
browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")
stockClick=browser.find_elements_by_class_name("clickable")
stockClick[num].find_element_by_tag_name("a").click()
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")

#株価のスクレイピング
if len(stockLine)==302:
KabukaComparisons=[]
for i in range(2,152):
stockKabukaPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
stockKabukaPriceBefore=stockLine[i].find_elements_by_tag_name("td")
KabukaComparison=float(stockKabukaPriceAfter[6].text)-float(stockKabukaPriceBefore[6].text)
KabukaComparisons.append(KabukaComparison)
stockKabukaPriceAfter=stockLine[151].find_elements_by_tag_name("td")
stockKabukaPriceBefore=stockLine[153].find_elements_by_tag_name("td")
KabukaComparison=float(stockKabukaPriceAfter[6].text)-float(stockKabukaPriceBefore[6].text)
KabukaComparisons.append(KabukaComparison)
for i in range(154,302):
stockKabukaPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
stockKabukaPriceBefore=stockLine[i].find_elements_by_tag_name("td")
KabukaComparison=float(stockKabukaPriceAfter[6].text)-float(stockKabukaPriceBefore[6].text)
KabukaComparisons.append(KabukaComparison)
KabukaComparisonsTable.append(KabukaComparisons)

#銘柄名の取得
stockTitleBox=browser.find_element_by_class_name("base_box_ttl")
stockTitle=stockTitleBox.find_element_by_class_name("jp").text
columnNames.append(stockTitle)

#ランキングテーブルの取得
KabukaTable=pd.DataFrame(KabukaComparisonsTable)
KabukaTable=ETFTable.T
KabukaTable.columns=columnNames

#ランキングテーブルの確認
KabukaTable.head()

#銘柄の選択
meigara_number = 8848
meigara_name = "レオパレス21"

#日付データのスクレイピング
browser=webdriver.Chrome()
browser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(1,152):
stockDate=stockLine[i].find_elements_by_tag_name("td")
stockDate=stockDate[0].text
dates.append(stockDate)
for i in range(153,302):
stockDate=stockLine[i].find_elements_by_tag_name("td")
stockDate=stockDate[0].text
dates.append(stockDate)
df_date=pd.DataFrame()
df_date["date"]=dates
df_date["year"]=df_date["date"].apply(lambda x:int(x.split("-")[0]))
df_date["month"]=df_date["date"].apply(lambda x:int(x.split("-")[1]))
df_date["day"]=df_date["date"].apply(lambda x:int(x.split("-")[2]))
df_date.head()

#株価前日比の取得
browser=webdriver.Chrome()
browser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
targetStockComparisons=[]
for i in range(2,152):
targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)
targetStockPriceAfter=stockLine[151].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[153].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)
for i in range(154,302):
targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")
targetStockPriceBefore=stockLine[i].find_elements_by_tag_name("td")
targetStockComparison=float(targetStockPriceAfter[6].text)-float(targetStockPriceBefore[6].text)
targetStockComparisons.append(targetStockComparison)
df=pd.DataFrame(targetStockComparisons)
df.columns=[meigara_name + "：前日比"]
df.head()

#データの統合
stockPriceTable=pd.concat([df_date,ETFTable],axis=1)
stockPriceTable=pd.concat([stockPriceTable,df],axis=1)
stockPriceTable.head()

#翌日のレオパレスの株価の指定
df_next=df.copy()
df_next.columns=[meigara_name + "：翌日比"]

#レオパレスの株価のスクレイピングbrowser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
dates=[]
for i in range(2,152):
stockDate=stockLine[i].find_elements_by_tag_name("td")
stockDate=stockDate[0].text
dates.append(stockDate)
for i in range(153,302):
stockDate=stockLine[i].find_elements_by_tag_name("td")
stockDate=stockDate[0].text
dates.append(stockDate)
df_date2=pd.DataFrame()
df_date2["date"]=dates

#レオパレスの株価テーブルの作成
df_next=pd.concat([df_date2,df_next],axis=1)
df_next.index=df_date2["date"]

#データの統合
table=stockPriceTable[1:299].copy()
table.index=table["date"]

#統合されたデータの表示
table[meigara_name + "：翌日比"]=df_next[meigara_name + "：翌日比"]
table.tail()

#csvとして出力
table.to_csv("stockPriceData.csv",index=False)

#再び必要なモジュールのインストール
import seaborn as sns
%matplotlib inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from selenium import webdriver
import requests
import json

#csvファイルの読み込み
train=pd.read_csv("stockPriceData.csv")
train.head()
df = pd.read_csv('stockPriceData.csv')
ooo = df[:0]
del(ooo['date'])
del(ooo['year'])
del(ooo['month'])
del(ooo['day'])
ppp = [meigara_name + '：前日比', meigara_name + '：翌日比']
kkk = ooo.columns
zzz = kkk.drop(ppp)
vars(zzz)

#機械学習の準備
features=['6138 ダイジェット工業(株)', '5009 富士興産(株)', '6185 ソネット・メディア・ネットワークス(株)',

        '3667 (株)ｅｎｉｓｈ', '9265 ヤマシタヘルスケアホールディングス(株)', '7238 曙ブレーキ工業(株)',

        '4463 日華化学(株)', '7191 (株)イントラスト', '3627 ネオス(株)',

        '3561 (株)力の源ホールディングス', '7730 マニー(株)', '2809 キユーピー(株)',

        '7475 アルビス(株)', '6189 (株)グローバルキッズＣＯＭＰＡＮＹ', '2424 (株)ブラス',

        '3932 (株)アカツキ', '3877 中越パルプ工業(株)', '9716 (株)乃村工藝社', '8349 (株)東北銀行',

        '9325 (株)ファイズ', '4680 (株)ラウンドワン', '7504 (株)高速',

        '8798 (株)アドバンスクリエイト', '4320 (株)ＣＥホールディングス', '7888 三光合成(株)',

        '8585 (株)オリエントコーポレーション', '3677 (株)システム情報',

        '5698 (株)エンビプロ・ホールディングス', '1726 (株)ビーアールホールディングス',

        '6330 東洋エンジニアリング(株)', '3771 (株)システムリサーチ',

        '8028 ユニー・ファミリーマートホールディングス(株)', '8589 (株)アプラスフィナンシャル',

        '6274 ヤマハモーターロボティクスホールディングス(株)', '7823 (株)アートネイチャー',

        '4369 (株)トリケミカル研究所', '8515 アイフル(株)', '3918 ＰＣＩホールディングス(株)',

        '3030 (株)ハブ', '7199 プレミアグループ(株)', '3992 (株)ニーズウェル', '2009 鳥越製粉(株)',

        '6740 (株)ジャパンディスプレイ', '7455 (株)三城ホールディングス',

        '7735 (株)ＳＣＲＥＥＮホールディングス', '6753 シャープ(株)', '2931 (株)ユーグレナ',

        '7481 尾家産業(株)']

x=train[features]
y=train[meigara_name + "：翌日比"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.27)

#モデリングと予測
model=RandomForestRegressor(n_estimators=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

#結果の表示
testUpDown=[]
for test in y_test:
if test>0:
testUpDown.append(1)
else:
testUpDown.append(-1)
predUpDown=[]
for pred in y_pred:
if pred>0:
predUpDown.append(1)
else:
predUpDown.append(-1)
print("確率："+str(metrics.accuracy_score(testUpDown,predUpDown)*100)+"%")

#特徴量のグラフの出力
feature_imp = pd.Series(model.feature_importances_,index=features).sort_values(ascending=False)
print(feature_imp)
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.figure(figsize=(30,50))
plt.show()

#Slackへ
slackURL="https://hooks.slack.com/services/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"
def send_slack(content):
payload={

        "text":content,

        "username":"PythonStockForecast",

        "icon_emoji":":snake:"

    }

    data=json.dumps(payload)

    requests.post(slackURL,data)

send_slack(resultNotification)