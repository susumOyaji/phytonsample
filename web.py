import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from selenium  import webdriver  #Selenium Webdriverをインポートして




url = "https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3"  #リストから銘柄を選択
urlName = "https://business.nikkei.com"
headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
print(text)  
  
print(soup.prettify)
tag_span = soup.find_all('span')
for elem in tag_span: 
  try:
    string = elem.get("class").pop(0)
    if string in "category":#<span class="category">小田嶋隆の「ア・ピース・オブ・警…</span>
      #print(elem.string)
      title = elem.find_next_sibling("h3")
      #print(title.text.replace('\n',''))
      r = elem.find_previous('a')
      #print(urlName + r.get('href'), '\n')
  except:
    pass


#browser = webdriver.Chrome()
#for num in range(0,1):
#browser.get("https://kabuoji3.com/ranking/?date=2019-07-05&type=1&market=3")  #リストから銘柄を選択
#print(browser.page_source)  
#stockClick=soup.find_elements_by_class_name("clickable")
#stockClick[num].find_element_by_tag_name("a").click()
#stockTable = soup.find_element_by_class_name("table_wrap")
#stockLine = stockTable.find_elements_by_tag_name("tr")


tag_tr = soup.find_all('tr')
for num in range(0, 1):
  try:  
      head = [h.text for h in tag_tr[0].find_all('th')]
      data = []
      for i in range(1,len(tag_tr)):
        data.append([d.text for d in tag_tr[i].find_all('td')])
        df = pd.DataFrame(data, columns=head)
  except IndexError:
    pass#print('No data')




