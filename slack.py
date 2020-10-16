# coding: UTF-8

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time





def get_htmls(stock_number):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  #print(text)
  #print(soup)  
  # 平均の値を取得する
  #print soup.select_one("#heikin")


  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[1])
  print(data[2])
  print('')
  #data = []
  #for i in range(1,len(tag_tr)):
    #data.append([d.text for d in tag_tr[i].find_all('td')])

  #df = pd.DataFrame(data, columns=head)
    # except IndexError:
    #    print('No data')




def get_Year_to_date_highs():
  urlName ='https://info.finance.yahoo.co.jp/ranking/?kd=29&mk=3&tm=d&vl=a'#年初来高値
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  data1 = [d.text for d in soup.find_all('td')]
  #for i in range(1, len(data1)):
  #  print('年初来高値: '.decode('utf-8')+data1[i])
  return data1

def  Price_drop():
  urlName = 'https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=3&tm=d&vl=a'#値上がり率
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text = soup.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  data2 = [d.text for d in soup.find_all('td')]
  #for i in range(1,len(data2)):
  #  #print('値上がり率: '.decode('utf-8') + data2[i])
  return data2

def Volume_per_unit():
  urlName ='https://info.finance.yahoo.co.jp/ranking/?kd=32&mk=3&tm=d&vl=a'#単元当たり出来高  
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text = soup.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  data3 = [d.text for d in soup.find_all('td')]
  #for i in range(1,len(data3)):
    #print('単元当たり出来高: '.decode('utf-8') + data3[i])
  return data3


def Stop_High():
  urlName = 'https://info.finance.yahoo.co.jp/ranking/?kd=27&mk=3&tm=d&vl=a'#ストップ高  
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text = soup.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  data4 = [d.text for d in soup.find_all('td')]
  #for i in range(1,len(data4)):
    #print('ストップ高: '.decode('utf-8') + data4[i])
  return data4
 




#リストから銘柄を選択/株価ランキングデータ
#urllist = "https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3"
#再び必要なモジュールのインストール
import seaborn as sns
#%matplotlib inline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
#from selenium import webdriver
import requests
import json



#銘柄の選択
meigara_number = 8848
meigara_name = "レオパレス21"

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
features=['6138 ダイジェット工業(株)', '5009 富士興産(株)', '6185 ＳＭＮ(株)','3667 (株)ｅｎｉｓｈ', ]

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
#plt.xlabel('Feature Importance Score')
#plt.ylabel('Features')
#plt.title("Visualizing Important Features")
#plt.figure(figsize=(30,50))
#plt.show()

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

#send_slack(resultNotification)
'''
print(pandas.__vesion__)
print(numpy.__vesion__)
print(matplotlib.__vesion__)
print(sklearn.__vesion__)
'''

















  



stack_code = ['6758', '6976', '4755','4661']
data1 = ''

while False:
  #複数のデータフレームをcsvで保存
  for i in stack_code:
    get_htmls(i)





  highs = get_Year_to_date_highs()
  volume = Volume_per_unit()
  price = Price_drop()
  stop = Stop_High()
    
  print('')
  print('年初来高値: ' + highs[2])
  print(' stockPrice: '+highs[4])
  print(' Hi_stockPrice: ' + highs[7])
  print('')
  print('単元当たり出来高: ' + volume[3])
  print(' Trading value: ' + volume[5])
  print(' Volume per unit: ' + volume[8])
  print('')
  print('値上がり率: ' + price[3])
  print(' stockPrice: ' + price[7])
  print('')
  if stop:
    print('ストップ高: ' + stop[2])
    print('stockPrice' + stop[6])
  else:  
    print('ストップ高:  non')
  print('')
  time.sleep(60)














#browser = webdriver.Chrome()
#for num in range(0,1):
#browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")  #リストから銘柄を選択
#print(browser.page_source)  
#stockClick=soup.find_elements_by_class_name("clickable")
#stockClick[num].find_element_by_tag_name("a").click()
#stockTable = soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")






