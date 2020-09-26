import requests
import pandas as pd
from bs4 import BeautifulSoup



html=requests.get("https://www.updateurself.com/2019/11/14/the-way-to-challenge/").text
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify)

#1, scriptやstyleを含む要素を削除する
for script in soup(["script", "style"]):
    script.decompose()#削除のメソッドです。
print(soup)

#2, テキストのみを取得=タグは全部取る
text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
print(text)


#3, textを改行ごとにリストに入れて、リスト内の要素の前後の空白を削除
lines = [line.strip() for line in text.splitlines()]

lines=[]
for line in text.splitlines():
  lines.append(line.strip)
print(lines)


#4, リストの空白要素以外をすべて文字列に戻す
#text="\n".join(line for line in lines if line)