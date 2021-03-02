from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
import japanize_kivy




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







class user(Screen):
    def add_more(self):
        self.ids.rows.add_row()


    #Newyork dow

    #Nikkei25

    #MyItem
    #企業コード nikkei,sony,taiyou,rukten
    code = ['998407','6758', '6976', '4755'] 
    price = ['0','1665', '1801', '1137'] #購入単価
    quantity = [1, 200, 300, 400] #数量
    
    Marketprice = [] #個別時価総額=数量ｘ時価
    name = [] #企業名
    price = [] #購入単価
   
    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        price.append(responce[1])

    
    for i in range(len(code)):
        try:
            Marketprice.append(float(price[i].replace(',', '')) * quantity[i])
        except ZeroDivisionError:
            print('You can not do this operation!')
   
    #Label1
    seconds_string = '  Stack Card'

    #Label2
    newyork = 'NewYork Dow \n$' + ' In earnest program'
    
    #Label3
    nikei225 = name[0] + '\n¥' + price[1] + '\n¥' + str(Marketprice[1])

    #Label4
    rakuten = name[3] + '\n¥' + price[3] + '\n¥' + str(Marketprice[3])




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
        #self.root = Builder.load_file('Demo.kv')
        self.root = Builder.load_file('floatlayout.kv')
        self.title = 'Python to Iphone App'
        return self.root


if __name__ == '__main__':
    Test1().run()