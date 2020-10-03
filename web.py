import requests
import pandas as pd
from bs4 import BeautifulSoup






def get_htmls(stock_number):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  #print(text)
  #print(soup)  

  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[1])
  #print(data[2])
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
  



stack_code = ['6758', '6976', '4755']
data1 = ''

#複数のデータフレームをcsvで保存
#for i in stack_code:
#  get_htmls(i)


highs = get_Year_to_date_highs()
volume = Volume_per_unit()
price = Price_drop()
stop = Stop_High()
print('')
print('年初来高値: '.decode('utf-8') + highs[2])
print(' stockPrice: '+highs[4])
print(' Hi_stockPrice: ' + highs[7])
print('単元当たり出来高: '.decode('utf-8') + volume[3])
print(' Trading value: ' + volume[5])
print(' Volume per unit: ' + volume[8])
print('値上がり率: '.decode('utf-8') + price[3])
print(' stockPrice: ' + price[7])
print('ストップ高: '.decode('utf-8') + stop[2])
print(' stockPrice: ' + stop[6])











#browser = webdriver.Chrome()
#for num in range(0,1):
#browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")  #リストから銘柄を選択
#print(browser.page_source)  
#stockClick=soup.find_elements_by_class_name("clickable")
#stockClick[num].find_element_by_tag_name("a").click()
#stockTable = soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")






