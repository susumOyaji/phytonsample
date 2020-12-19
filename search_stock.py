import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
from selenium import webdriver
import chromedriver_binary


def sample():
  print('sample')

  
def get_stock_list(low, high, target_code):
  print('get_stock_list to get_stock_list()')
  driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
  driver.get('https://stock.web0000.jp/') 
  time.sleep(5) # Let the user actually see something!
  
  
  month_elem = driver.find_element_by_id("input-57")
  month_elem.clear()
  month_elem.send_keys("12")
  