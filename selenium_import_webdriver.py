from selenium import webdriver
from selenium.webdriver.support.ui import Select

#%#
from bs4 import BeautifulSoup
import requests

'''
browser = webdriver.Chrome("chromedriver.exe")
browser.get("http://example.selenium.jp/reserveApp/")
browser.maximize_window()
'''
#def get_htmls(stock_number):
urlName = "http://example.selenium.jp/reserveApp/"
soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
text=soup.get_text()#.

#month_elem = soup.find_element_by_id("reserve_month")
month_elem = soup.find_all('reserve_month')
month_elem.clear()
month_elem.send_keys("8")


breakfast_off_elem = browser.find_element_by_id("breakfast_off")
breakfast_off_elem.click()



driver = webdriver.Chrome("C:\\tool\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("http://needtec.sakura.ne.jp/auto_demo/form1.html")
driver.find_element_by_name("name").send_keys("名前太郎");
driver.find_element_by_name("mail").send_keys("test@co.jp");
driver.find_element_by_name("comment").send_keys("猫猫子猫\n\r犬犬子犬");

# チェックボックス
chks = driver.find_elements_by_name("q1[]")
chks[0].click()
chks[2].click()

# オプションボタン
opts = driver.find_elements_by_name("men")
opts[1].click()

# 選択
sel = Select(driver.find_element_by_name("osi[]"))
sel.deselect_all()
sel.select_by_index(1)
sel.select_by_index(2)

# ボタン押下
driver.find_element_by_xpath("//input[@value='登録する']").click()
driver.switch_to.alert.accept()

# 結果
results = driver.find_elements_by_tag_name("tr")
for rec in results:
    print(rec.text)

driver.close()