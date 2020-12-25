import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
from selenium import webdriver
import chromedriver_binary



# pip install chromedriver-binary==87.0.4280.88
# pip install chromedriver-binary==75.0.3770.8.0 
urlName = 'https://stock.web0000.jp/'
driver = webdriver.Chrome()
def get_stock_list(low, high, target_code):
  #driver = webdriver.Chrome("c:/Users/chromedriver_win32/chromedriver.exe")  # Optional argument, if not specified will search path.
  
  
  driver.get(urlName) 

 
  
  #month_elem = driver.find_element_by_id("__nuxt")
  #fruit = driver.find_element_by_class_name('v-text-field__slot')
  month_elem = driver.find_element_by_id("input-47")
  month_elem.clear()
  month_elem.send_keys("1")

  month_elem = driver.find_element_by_id("input-50")
  month_elem.clear()
  month_elem.send_keys("2")

  month_elem = driver.find_element_by_id("input-53")
  month_elem.clear()
  month_elem.send_keys("6758")

  month_elem = driver.find_element_by_class_name("container")
  month_elem.click()

  



def get_stock_data(code):
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  #print(text)
  #print(soup)  
  print(soup.head.title)

  '''class属性が「colBoxTopstories」のdivタグを検索する'''
  #topstories = soup.find('div', class_='v-data-table__wrapper')
  topstories = soup.select('body')
  print(topstories)
  
  '''
  elems = soup.select('div',id='__layout')
  for elem in elems:
    print(elem)
  '''

  tag_tr = soup.find_all("tbody")
  head = [h.text for h in tag_tr[0].find_all('td')]


  tag_tr = soup.find_all('tr')

  month_elem = driver.find_element_by_id("__layout")
  month_elem = driver.find_element_by_class_name("v-data-table-header")
  #print('month',month_elem)
  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  #month_elem = driver.find_element_by_id("input-53")
  head = [h.text for h in tag_tr[0].find_all('td')]


  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[1])
  print(data[2])
  print('')



  return code


def get_ret_index(data):
  return data  



#'c:\users\seisan1\appdata\local\programs\python\python38\python.exe -m pip install --upgrade pip' command.








  
'''
  # 一番最初の「りんご」が返却される
  fruit = driver.find_element_by_class_name('fruit')
  # 一番最初の「りんご」「メロン」「桃」の全てがリストで返却される
  fruits = driver.find_elements_by_class_name('fruit')
  username = driver.find_element_by_name('username')
  password = driver.find_element_by_name('password')

  #このような条件が複雑な指定方法では find_element_by_css_selector を使うと良いでしょう。 ここではclass属性の親子関係関係に着目して要素を絞り込みます。
  apple = driver.find_element_by_css_selector('.menu .apple')
  '''
