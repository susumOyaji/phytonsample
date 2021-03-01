#-*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from bs4 import BeautifulSoup
import requests
#from kivy.core.window import Window
#from kivy.app import runTouchApp
from kivy.uix.button import Button

import japanize_kivy
from kivy.config import Config  # 追加


#Config.set('graphics', 'width', '900')  # 追加
#Config.set('graphics', 'height', '1320')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 2000)
Config.set('graphics', 'top',  10)

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (900, 1320)

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する
 #Labei1
    



class Creature(object):
    def __init__(self, level=1, weapon=None):
        self.level = level
        self.hp = 0
        self.mp = 0
        self.attack = 0
        self.defence = 0
        self.weapon = weapon
        self.job = "neet"

    def status(self):
        return "Job:{} | HP:{} | MP:{} | Atk:{} | Def:{} | Weapon:{}".format \
                (self.job, self.hp, self.mp, self.attack, self.defence, self.weapon)


class Warrior(Creature):
    def __init__(self, level):
        super().__init__(level)
        self.attack += 3 * level
        if self.weapon is None:
            self.weapon = "sword"
        if self.job == "neet":
            self.job = "Warrior"
        else: self.job += "Warrior"


class Magician(Creature):
    def __init__(self, level):
        super().__init__(level)
        self.mp += 4 * level
        if self.weapon is None:
            self.weapon = "rod"
        if self.job == "neet":
            self.job = "Magic"
        else: self.job += "Magic"   

'''
class User(Screen):

    def add_more(self):
        self.ids.rows.add_row()

    def sub_more(self):
        self.ids.rows.remove_row()    

'''

class Row(BoxLayout):
    buttonNo_text = StringProperty("")
    button_text = StringProperty("")
    

class Rows(BoxLayout):
    row_count = 0
    content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
        self.add_row()
        #self.remove_row()


    def add_row(self):



        self.row_count += 1
        self.add_widget(Row(buttonNo_text=str(self.row_count),button_text = str(Marketprice[self.row_count])))

    
    
    
    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1







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

 




class Mainscreen(BoxLayout):
    #企業コード nikkei,sony,taiyou,rukten
    code = ['998407','6758', '6976', '4755'] 
    price = ['0','1665', '1801', '1137'] #購入単価
    quantity = [1, 200, 300, 400] #数量
    
    Marketprice = []
    name = []
    price = []
   
    #while True:
    #複数のデータフレームをcsvで保存
    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        price.append(responce[1])

    
    for i in range(len(code)):
        Marketprice.append(float(price[i].replace(',', '')) * quantity[i])

   
    #Label1
    seconds_string = '  Stack Card'

    #Label2
    newyork = 'NewYork Dow \n$' + ' In earnest program'
    
    #Label3
    nikei225 = name[0] + '\n¥' + price[1] + '\n¥' + str(Marketprice[1])

    #Label4
    rakuten = name[1] + '\n¥' + price[2] + '\n¥' + str(Marketprice[3])

  
   
#class PasonalValue():

   




   

  

class FloatLayoutApp(App):
    def build(self):
        self.title = 'Stack Card(Python)'
        #self.root = Builder.load_file('floatlayout.kv')
  
        return Mainscreen()

if __name__=="__main__":
    FloatLayoutApp().run()









''''
             Button:
            text: 'Newyork Dow!'
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        Button:
            text: 'Nikkei225!'
            pos_hint: {'right': 1, 'y': 0}
           






class TextWidget(Widget):
    text  = StringProperty()
    color = ListProperty([0,0,0,0])




    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        
        

    def buttonClicked(self):
        self.text = 'おはよう'
        self.color = [1, 0, 0 , 1]

    def buttonClicked2(self):
        self.text = 'こんにちは'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked3(self):
        self.text = 'こんばんは'
        self.color = [0, 0, 1 , 1 ]

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'Python to Iphone App'
        self.text = 'start'


if __name__ == '__main__':
    TestApp().run()

'''