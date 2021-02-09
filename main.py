#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import japanize_kivy
from kivy.config import Config  # 追加


Config.set('graphics', 'width', '600')  # 追加
Config.set('graphics', 'height', '1000')  # 追加

# デフォルトに使用するフォントを変更する
#resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class TextWidget(Widget):
    text  = StringProperty()
    color = ListProperty([0,0,0,0])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'
        

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

if __name__ == '__main__':
    TestApp().run()

