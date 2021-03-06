#(main.py)


import re#正規表現

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.button import Button
#######
from kivy.config import Config  # 追加
from bs4 import BeautifulSoup
import requests
import japanize_kivy


Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '650')  # 追加
Config.set('graphics', 'height', '1350')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1400)
Config.set('graphics', 'top', 35)


#企業コード nikkei,sony,taiyou,rukten
code = ['6758', '6976', '4755'] 
price = [1665, 1801, 1137] #購入単価
quantity = [200, 300, 400] #数量
Marketprice = [] #個別時価総額=数量ｘ時価
value = [] #時価
name = [] #企業名
before = []
ratio = []
TotalValue = 0


def get_dowhtmls():
  urlName = 'https://finance.yahoo.co.jp/quote/%5EDJI'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('dd')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[3].find_all('span')]#th
  data = head[0]
  return data



def get_nikkeyhtmls():
  data = []  
  #urlName = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
  urlName = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('body')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[0].find_all('tr')]  #tr
 
  s = head[0]
  name = s[1:7]  # スライスで半角空白文字よりも前を抽出
  
  target = "\n前"
  idx = s.find(target)
  stock = s[12:idx]
  
  target = " \n"
  idx = s.find(target)
  ratio = s[16:idx]

  data.append(name)
  data.append(stock)
  data.append(ratio)
  return data


def get_htmls(stock_number):
  data = []

  urlName = "https://finance.yahoo.co.jp/quote/"+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  #text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  tag_tr = soup.find_all('body')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('span')]
  #print(head[0])#ソニー（株）
  s = head[81]
  target = "の"
  idx = s.find(target)
  r = s[:idx]  # スライスで半角空白文字よりも前を抽出

 
  data.append(r+head[17])
  data.append(head[22])
  data.append(head[29])
 
  print('Name: ',data[0])
  print('StoksPrice: ',data[1])
  print('The day before ratio: ',data[2])
  print('')
  return data


class AppRoot(BoxLayout):
    pat = re.compile(r'\.{3}')
    my_rv = ObjectProperty()
   
    
    def label_add(self, text):
        self.label_text.text = text

    def choose_data(self, btn):
        print(f"Index {btn.index}: {btn.text}")

    def create_data(self, btn):
        data_txt = self.pat.sub(self.ids.input.text.capitalize(), btn.text)
        self.my_rv.data.append({'text': data_txt})  # 2:

    


    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        value.append(responce[1])
        #before.append(responce[2]) #前日比
        ratio = responce[2].replace('前日比','')
        before.append(ratio)
        

    #Newyork dow
    dow = get_dowhtmls()
    #Label2
    newyork = 'NewYork Dow $' + dow
    #Nikkei25
    nikkei= get_nikkeyhtmls()
    #Label3
    nikei225 = nikkei[0] + nikkei[1] + '\n'+  nikkei[2]
    

    for i in range(len(code)):
        try:
            Marketprice.append(float(value[i].replace(',', '')) * quantity[i])
            TotalValue = TotalValue + Marketprice[i]
        except ValueError:
            Marketprice.append('---')
        
    #Label4
    TotalAsset= 'TotalAsset   ¥'+str("{:,}".format(TotalValue))



class MyRecycleBoxLayout(RecycleBoxLayout):
    def add_widget(self, widget, index=0, canvas=None):  # 4:
        widget.index = self.view_indices[widget]  # 6:
        if widget.index % 2:
            widget.background_color = 0, 0, 1, 0.5
        else:
            widget.background_color = 1, 0, 0, 0.5

        super().add_widget(widget, index, canvas)  # 5:



class ButtonWidget(MyRecycleBoxLayout):
    label_text = ObjectProperty(None)
    
    def label_add(self, text):
        self.label_text.text = text

class RVApp(App):
     def build(self):
        root = AppRoot()
        button = ButtonWidget()
        button.add_widget()
        return root
    #pass


    


#new = NewStyleClass()
#new.test_method('')

if __name__ == '__main__':
    RVApp().run()
