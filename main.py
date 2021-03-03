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


def get_dowhtmls():
  urlName = 'https://finance.yahoo.co.jp/quote/%5EDJI'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('dd')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[1].find_all('span')]#th
  data = head[0]
  return data





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






class Row(BoxLayout):
    button_text = StringProperty("")
    item_value = StringProperty("")


class Rows(BoxLayout):
    row_count = 0

    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
        self.add_row()


    def add_row(self):
        self.row_count += 1
        self.add_widget(Row(button_text=str(self.row_count),item_value=str(self.row_count)))
    

    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1



class user(Screen):
    #Newyork dow
    dow = get_dowhtmls()
    #Label2
    newyork = 'NewYork Dow $' + dow
    #Nikkei25
    nikkei= get_htmls('998407')
    #Label3
    nikei225 = nikkei[0] + '   ¥' + nikkei[1] #+ '\n¥' + str(Marketprice[0])
    #MyItem
    #企業コード nikkei,sony,taiyou,rukten
    code = ['6758', '6976', '4755'] 
    price = [1665, 1801, 1137] #購入単価
    quantity = [200, 300, 400] #数量
    
    Marketprice = [] #個別時価総額=数量ｘ時価
    name = [] #企業名
    value = [] #時価
    TotalValue = 0


    def add_more(self):
        self.ids.rows.add_row()


    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        value.append(responce[1])
        
    
        
    #Label1
    seconds_string = '  Stack Card'
    inst = Rows()
    inst.add_row()

    for i in range(len(code)):
        try:
            Marketprice.append(float(value[i].replace(',', '')) * quantity[i])
            TotalValue = TotalValue + Marketprice[i]
            ids.rows.add_row()

        except ValueError:
            newyork = '---'
            nikei225 = '---'
            rakuten='---'
            #print('You can not do this operation!')
    #Label4
    TotalAsset= 'TotalAsset   ¥'+str("{:,}".format(TotalValue))
    rakuten = name[2] + '\n¥' + str(price[2]) + '\n¥' + str(Marketprice[2])
              
    
    









class Test1(App):
    def build(self):
        #self.root = Builder.load_file('Demo.kv')
        self.root = Builder.load_file('floatlayout.kv')
        self.title = 'Python to Iphone App'
        return self.root


if __name__ == '__main__':
    Test1().run()