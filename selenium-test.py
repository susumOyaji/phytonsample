# coding:utf-8
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from time import sleep




driver = webdriver.Chrome()
driver.get(URL)
driver.close()
driver.quit()


# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://www.google.co.jp/")
# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_id("lst-ib").send_keys("selenium")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
# 5秒間待機してみる。
sleep(5)
# ブラウザを終了する。
driver.close()