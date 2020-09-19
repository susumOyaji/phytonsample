# 必要なライブラリのインポート
import time
from selenium import webdriver




import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


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
driver.find_element_by_link_text("Selenium - Web Browser Automation").click()

# 5秒待つ
time.sleep(5)

# Chromeブラウザを閉じる
driver.quit()