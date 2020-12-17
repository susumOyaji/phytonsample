import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime


def get_stock_list(low, high, target_code):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+target_code
  #https://stock.web0000.jp/
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
  print('No data')
  return

