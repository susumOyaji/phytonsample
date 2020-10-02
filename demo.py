# ライブラリの読み込み
from bs4 import BeautifulSoup
import requests
#必要なモジュールのインストール
#from selenium  import webdriver  #Selenium Webdriverをインポートして
import pandas as pd
from pandas import DataFrame
import numpy as np

#%matplotlib inline
#import matplotlib.pyplot as plt
import time
#from selenium import webdriver
 



#browser = webdriver.Chrome()
#browser = webdriver.Chrome('C:/Users/seisan1/AppData/Local/Pyhon/chromedriver_win32/chromedriver')#driver = webdriver.Chrome('/usr/local/bin/chromedriver')
columnNames=[]
#ETFComparisonsTable = []
KabukaComparisonsTable = []

for num in range(0,1):
    url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6758"  #^DJI
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    print(soup)
    #text=soup.get_text()
    #browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")#リストから銘柄を選択
    
    #stockClick=soup.find_elements_by_class_name("clickable")
    #stockClick[num].find_element_by_tag_name("a").click()
    #stockTable=browser.find_element_by_class_name("table_wrap")
    #stockLine=stockTable.find_elements_by_tag_name("tr")
    #try:
    #    url = "https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3"#ランキングデータ
    #    soup = BeautifulSoup(requests.get(url).content,'html.parser')
    
    tag_tr = soup.find_all('tr')
    head = [h.text for h in tag_tr[0].find_all('th')]
    data = []
    for i in range(1,len(tag_tr)):
        data.append([d.text for d in tag_tr[i].find_all('td')])
            #df = pd.DataFrame(data, columns=head)
    # except IndexError:
    #    print('No data')


            


    #株価のスクレイピング
    if len(tag_tr)==302:
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
KabukaTable=KabukaTable.T#ETFTable.T
KabukaTable.columns=columnNames

#ランキングテーブルの確認
KabukaTable.head()

#銘柄の選択
meigara_number = 8848
meigara_name = "レオパレス21"

#日付データのスクレイピング
#browser=webdriver.Chrome()
#browser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
#stockTable=soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")

url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6758"  #^DJI
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
tag_tr = soup.find_all('tr')
head = [h.text for h in tag_tr[0].find_all('th')]
data = []
for i in range(1,len(tag_tr)):
    data.append([d.text for d in tag_tr[i].find_all('td')])


dates=[]
for i in range(1,152):
    stockDate=soup.find_elements_by_tag_name("td")
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
#browser=webdriver.Chrome()
browser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
stockTable=browser.find_element_by_class_name("table_wrap")
stockLine=stockTable.find_elements_by_tag_name("tr")
targetStockComparisons=[]
for i in range(2,152):
    targetStockPriceAfter=stockLine[i-1].find_elements_by_tag_name("td")#(-1)前日
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
stockPriceTable=pd.concat([df_date,KabukaTable],axis=1)
stockPriceTable=pd.concat([stockPriceTable,df],axis=1)
stockPriceTable.head()

#翌日のレオパレスの株価の指定   
df_next=df.copy()
df_next.columns=[meigara_name + "：翌日比"]

#レオパレスの株価のスクレイピング
browser.get("https://kabuoji3.com/stock/{}/".format(meigara_number))
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
df_next=pd.concat([df_date2,df_next],axis=1)#連結するオブジェクトを指定
df_next.index=df_date2["date"]

#データの統合
table=stockPriceTable[1:299].copy()
table.index=table["date"]

#統合されたデータの表示
table[meigara_name + "：翌日比"]=df_next[meigara_name + "：翌日比"]
table.tail()

#csvとして出力
table.to_csv("stockPriceData.csv",index=False)

print(table)
