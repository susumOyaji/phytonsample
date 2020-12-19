# 必要なライブラリのインポート
import time
from selenium import webdriver
import chromedriver_binary


#pip install chromedriver-binary==87.0.4280.88

#import time
#from selenium import webdriver
#セッションが作成されていません: このバージョンの ChromeDriver は Chrome バージョン 85 のみをサポートしています
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://example.selenium.jp/reserveApp/')
#time.sleep(1) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(15) # Let the user actually see something!
#driver.quit()



month_elem = driver.find_element_by_id("reserve_month")
month_elem.clear()
month_elem.send_keys("8")
 
day_elem = driver.find_element_by_id("reserve_day")
day_elem.clear()
day_elem.send_keys("2")
 
term_elem = driver.find_element_by_id("reserve_term")
term_elem.clear()
term_elem.send_keys("3")
 
breakfast_off_elem = driver.find_element_by_id("breakfast_off")
breakfast_off_elem.click()
 
plan_a_elem = driver.find_element_by_id("plan_a")
plan_a_elem.click()
 
plan_b_elem = driver.find_element_by_id("plan_b")
plan_b_elem.click()
 
name_elem = driver.find_element_by_id("guestname")
name_elem.send_keys("エドワイズ")
 
next_elem = driver.find_element_by_id("goto_next")
next_elem.click()
 
commit_elem = driver.find_element_by_id("commit")
commit_elem.click()






#id で取得
driver.find_element_by_id('ID')

#class で取得
driver.find_element_by_class_name('CLASS_NAME')

#name で取得
driver.find_element_by_name('NAME')

#link textで取得
driver.find_elements_by_link_text('LINK_TEXT')

#ネストされた要素は path を指定して取得
driver.find_elements_by_xpath(".//a")


# Chromeブラウザを起動する
driver = webdriver.Chrome()

# Googleのサイトを開く
driver.get("https://www.google.co.jp/")

# 検索ワードを入力する場所を探して「Selenium」と入力する
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')

# 検索を実行する（検索ボタンを押すのと同じ動作）
search_box.submit()

# 検索結果からタイトルが「Selenium - Web Browser Automation」のリンクをクリックする。
driver.find_element_by_link_text("Webの操作を自動化してくれる「Selenium」を使ってみた ...").click()

# 5秒待つ
time.sleep(5)

# Chromeブラウザを閉じる
driver.quit()