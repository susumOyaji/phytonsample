from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty




#######
from kivy.config import Config  # 追加
from bs4 import BeautifulSoup
import requests
#Config.set('graphics', 'width', '900')  # 追加
#Config.set('graphics', 'height', '1320')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 2000)
Config.set('graphics', 'top',  10)

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (900, 1320)



def get_htmls(stock_number):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  #text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  #print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  data[0] = head[0]
 
  print('Name: ',data[0])
  print('StoksPrice: ',data[1])
  print('The day before ratio: ',data[2])
  print('')
  return data







class User(Screen):

    NewYork=''
    Nikkei='nikkei'
    Assets=0

    def add_more(self):
        self.ids.rows.add_row()

    def sub_more(self):
        self.ids.rows.remove_row()

    code = ['998407','6758', '6976', '4755'] #企業コード
    price = ['0','6758', '6976', '4755'] #購入単価
    quantity = [1,6758, 6976, 4755] #数量

    
    name = []
    price = []
    Marketprice = []


    #while True:
    #複数のデータフレームをcsvで保存
    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        price.append(responce[1])

    
    for i in range(len(code)):
        Marketprice.append(float(price[i].replace(',', '')) * quantity[i])

    NewYork = Marketprice[0]
    #highs = get_Year_to_date_highs()
    #volume = Volume_per_unit()
    #price = Price_drop()
    #stop = Stop_High()
    #only = Only_Price()
    #post= Posted_version()




class Row(BoxLayout):
    button_text = StringProperty("")


class Rows(BoxLayout):
    row_count = 0

    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
        self.add_row()

    def add_row(self):
        self.row_count += 1
        self.add_widget(Row(button_text=str(self.row_count)))
    
    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1





class Test1(App):
    def build(self):
        self.root = Builder.load_file('Demo.kv')
        
        return self.root


if __name__ == '__main__':
    Test1().run()