#-*- coding: utf-8 -*-
import kivy
kivy.require('2.0.0')

#from kivy.clock import Clock
#from kivy.core.window import Window
from kivy.app import App
from bs4 import BeautifulSoup
import requests
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

#from kivy.core.window import Window
#from kivy.app import runTouchApp
from kivy.uix.button import Button

import japanize_kivy
from kivy.config import Config  # 追加


Config.set('graphics', 'width', '900')  # 追加
Config.set('graphics', 'height', '1320')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 2000)
Config.set('graphics', 'top',  100)

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する
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


class User(Screen):

    def add_more(self):
        self.ids.rows.add_row()

    def sub_more(self):
        self.ids.rows.remove_row()    


class Row(BoxLayout):
    button_text = StringProperty("")
   

class Rows(BoxLayout):
    row_count = 0
    
    content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
        self.add_row()

    def add_row(self):
        self.row_count += 1
        self.add_widget(Row(button_text=str(self.row_count)))     
            
    #self.add_widget(Row(button_text=str(self.row_count)))

    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1







def get_htmls(stock_number):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[1])
  print(data[2])
  print('')
  return data
 




class Mainscreen(Screen):
    def add_more(self):
        self.ids.rows.add_row()

    def sub_more(self):
        self.ids.rows.remove_row()

    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1
        
    #pass
   
    
    
  
        



    #Labei1
    seconds_string = '  Stack Card'


    #Label2
    NewYorkDow = '6758'
    Newyork_responce = get_htmls(NewYorkDow)
    newyork1 = Newyork_responce[1]
    newyork2 = Newyork_responce[2]
    newyork = 'NewYork Dow \n$' + newyork1 + '  ' + newyork2
    


    #Label3
    rakuten = '4755'
    rakuten_responce = get_htmls(rakuten)
    rakuten1 = rakuten_responce[1]
    rakuten2 = rakuten_responce[2]
    nikei225 = 'Nikei225 \n$' + rakuten1  + '  ' + rakuten2
    rakuten = 'Rakuten \n$' + rakuten1  + '  ' + rakuten2

    sony = '7698'

   

   




   

  

class FloatLayoutApp(App):
    def build(self):
        self.title = 'Stack Card(Python)'
        #self.root = Builder.load_file('floatlayout.kv')
        print(Warrior(5).status())
            #Job:Warrior | HP:0 | MP:0 | Atk:15 | Def:0 | Weapon:sword
        print(Magician(5).status())
            #Job:Magic | HP:0 | MP:20 | Atk:0 | Def:0 | Weapon:rod
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