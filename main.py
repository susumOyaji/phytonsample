#-*- coding: utf-8 -*-
import kivy
#kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.uix.label import Label
#from kivy.properties import StringProperty, ListProperty

#from kivy.core.text import LabelBase, DEFAULT_FONT
#from kivy.resources import resource_add_path
#from kivy.graphics import Color
#from kivy.graphics import Rectangle
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout


import japanize_kivy
from kivy.config import Config  # 追加


Config.set('graphics', 'width', '500')  # 追加
Config.set('graphics', 'height', '1200')  # 追加

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class TextWidget(Widget):
    pass
    #text  = StringProperty()
    #color = ListProperty([0,0,0,0])


class TestApp(App):
    def build(self):
        return TextWidget()
    

#class TestApp(App):
#    def __init__(self, **kwargs):
#        super(TestApp, self).__init__(**kwargs)
#        self.title = 'Python to Iphone App'
#        self.text = 'start'


if __name__ == '__main__':
    TestApp().run()

