import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
from selenium import webdriver
#import chromedriver_binary


def sample():
  print('sample')

  
def get_stock_list(low, high, target_code):
  print('get_stock_list to get_stock_list()')
  driver = webdriver.Chrome("c:/Users/chromedriver_win32/chromedriver.exe")  # Optional argument, if not specified will search path.
  driver.get('https://stock.web0000.jp/') 
  time.sleep(0) # Let the user actually see something!
  
  
  #month_elem = driver.find_element_by_id("__nuxt")
  #fruit = driver.find_element_by_class_name('v-text-field__slot')
  month_elem = driver.find_element_by_id("input-47")
  month_elem.clear()
  month_elem.send_keys("12")

  month_elem = driver.find_element_by_id("input-50")
  month_elem.clear()
  month_elem.send_keys("24")

  month_elem = driver.find_element_by_id("input-53")
  month_elem.clear()
  month_elem.send_keys("6758")

  month_elem = driver.find_element_by_class_name("v-btn__content")
  #month_elem.clear()
  month_elem.click()
  
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