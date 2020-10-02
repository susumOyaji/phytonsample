
import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する
html.responce = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=" + 6758
#load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")



# title、h2、liタグを検索して表示する
print(soup.find("title"))    # タグを検索して表示
print(soup.find("h2"))
print(soup.find("li"))
print(soup.find("title").text)    # .textを追加
print(soup.find("h2").text)
print(soup.find("li").text)
# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):    # すべてのliタグを検索して表示
    print(element.text)

# IDで検索して、そのタグの中身を表示する
chap2 = soup.find(id="chap2")    # idが「chap2」の範囲の要素を表示
for element in chap2.find_all("li"):    # その中のliタグの文字列を表示
    print(element.text)


# HTML全体を表示する
#print(soup)

# 
#<!DOCTYPE html>
#<html>
#	<head>
#		<meta charset="UTF-8">
#		<title>Python2年生</title>
#	</head>
#	<body>
#		<h2>第1章 Pythonでデータをダウンロード</h2>
#		<ol>
#			<li>スクレイピングってなに？</li>
#			<li>Pythonをインストールしてみよう</li>
#			<li>requestsでアクセスしてみよう</li>
#		</ol>
#	</body>
#</html>
# 

#<!DOCTYPE html>
#<html>
#	<head>
#		<meta charset="UTF-8">
#		<title>Python2年生</title>
#	</head>
#	<body>
#		<div id="chap1">
#			<h2>第1章 Pythonでデータをダウンロード</h2>
#			<ol>
#				<li>スクレイピングってなに？</li>
#				<li>Pythonをインストールしてみよう</li>
#				<li>requestsでアクセスしてみよう</li>
#			</ol>
#		</div>
#		<div id="chap2">
#			<h2>第2章 HTMLを解析しよう</h2>
#			<ol>
#				<li>HTMLを解析してみよう</li>
#				<li>ニュースの最新記事一覧を取得してみよう</li>
#				<li>リンク一覧をファイルに書き出そう</li>
#				<li>画像を一括ダウンロードしよう</li>
#			</ol>
#		</div>
#
#		<a href="https://www.ymori.com/books/python2nen/test1.html">リンク1</a>
#		<a href="./test3.html">リンク2</a><br/>
#		<img src="https://www.ymori.com/books/python2nen/sample1.png">
#		<img src="./sample2.png">
#		<img src="./sample3.png">
#	</body>
#</html>