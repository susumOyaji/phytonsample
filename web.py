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
  print(data[2])
  #data = []
  #for i in range(1,len(tag_tr)):
    #data.append([d.text for d in tag_tr[i].find_all('td')])

  #df = pd.DataFrame(data, columns=head)
    # except IndexError:
    #    print('No data')



def get_hiprice():
  urlName ='https://info.finance.yahoo.co.jp/ranking/?kd=29&mk=3&tm=d&vl=a'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  #print(text)
  print(soup)  

  tag_tr = soup.find_all('tr')
  print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[0])
  print(data[2])

stack_code = ['6758','6976','4755']

#複数のデータフレームをcsvで保存
#for i in stack_code:
  #get_htmls(i)
get_hiprice() 















#browser = webdriver.Chrome()
#for num in range(0,1):
#browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")  #リストから銘柄を選択
#print(browser.page_source)  
#stockClick=soup.find_elements_by_class_name("clickable")
#stockClick[num].find_element_by_tag_name("a").click()
#stockTable = soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")






