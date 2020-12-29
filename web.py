# coding: UTF-8

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime




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


def Only_Price():
  urlName = 'https://info.finance.yahoo.co.jp/ranking/?kd=6&tm=d&vl=a&mk=3&p=1'#単元株価格上位  
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text = soup.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  data5 = [d.text for d in soup.find_all('td')]
  return data5

def Posted_version():
  urlName = 'https://info.finance.yahoo.co.jp/ranking/?kd=56&mk=3&tm=d&vl=a'#掲示板  
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text = soup.get_text()  #.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  data6 = [d.text for d in soup.find_all('td')]
  return data6



 
  



stack_code = ['998407','6758', '6976', '4755']
data1 = ''

while True:
  #複数のデータフレームをcsvで保存
  for i in stack_code:
    get_htmls(i)


  highs = get_Year_to_date_highs()
  volume = Volume_per_unit()
  price = Price_drop()
  stop = Stop_High()
  only = Only_Price()
  post= Posted_version()
  '''  
  print('')
  print('年初来高値: ' + highs[2])
  print(' stockPrice: '+highs[4])
  print(' Hi_stockPrice: ' + highs[7])
  print('')
  
  if volume:
    print('単元当たり出来高: ' + volume[3]+' Trading value: ' + volume[5]+' Volume per unit: ' + volume[8])
    print('単元当たり出来高: ' + volume[13]+' Trading value: ' + volume[15]+' Volume per unit: ' + volume[18])
  else:
    print('単元当たり出来高: non')
  
  print('')
  print('値上がり率: ', price[3])
  print(' stockPrice: ',price[7])
  print('')
  
  if stop:
    print('ストップ高: ',stop[2])
    print('stockPrice',stop[6])
  else:  
    print('ストップ高:  non')
  '''  
  print('')
  #print('単元株価格上位',only[3],only[5])

  print('掲示板投稿数')
  for i in range(0,105,7) :
    print(post[i],post[i+1],post[i+3],post[i+5])
  
  dt_now = datetime.datetime.now()
  print(dt_now)
  
# 2019-02-04 21:04:15.412854
  time.sleep(60)













#browser = webdriver.Chrome()
#for num in range(0,1):
#browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")  #リストから銘柄を選択
#print(browser.page_source)  
#stockClick=soup.find_elements_by_class_name("clickable")
#stockClick[num].find_element_by_tag_name("a").click()
#stockTable = soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")






