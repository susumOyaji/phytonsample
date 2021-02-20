#-*- coding: utf-8 -*-
import kivy
kivy.require('2.0.0')

#from kivy.clock import Clock
#from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


import japanize_kivy
from kivy.config import Config  # 追加


Config.set('graphics', 'width', '600')  # 追加
Config.set('graphics', 'height', '1000')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 2000)
Config.set('graphics', 'top',  100)

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する




class Mainscreen(GridLayout):
    def __init__(self, label1, label2, label3):
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
       

    def status(self):
        return "Job:{} | HP:{} | MP:{} | Atk:{} | Def:{} | Weapon:{}".format \
                (self.job, self.hp, self.mp)

    #pass



class Pricedisp(Mainscreen):
    seconds_string = 'Stack Card'
    newyork = 'New York Dow Price $30,000'
    #nikei225 = 'Nikei225 Price ¥30,000'


     
   

  

class FloatLayoutApp(App):
    def build(self):
        self.title = 'Stack Card(Python)'        
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