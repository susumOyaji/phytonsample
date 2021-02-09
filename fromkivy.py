from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import ScatterPlane
from kivy.uix.label import Label
from bs4 import BeautifulSoup
import requests
from kivy.config import Config  # 追加
from kivy.properties import StringProperty  # 追加
from kivy.uix.widget import Widget  # 追加
from kivy.properties import StringProperty,ListProperty
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path


import japanize_kivy
#import pndas as pd

Config.set('graphics', 'width', '600')  # 追加
Config.set('graphics', 'height', '1000')  # 追加





def get_htmls(stock_number):
  urlName = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code="+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  #print(text)
  #print(soup)  
  # 平均の値を取得する
  #print soup.select_one("#heikin")


  tag_tr = soup.find_all('tr')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('th')]
  print(head[0])#ソニー（株）
  data = [d.text for d in tag_tr[0].find_all('td')]
  print('stoksPrice: '+data[1])
  print(data[2])
  print('')
 
  return data



class MainScreen(BoxLayout): #ユーザーインタフェースを記述するクラス
    text = StringProperty()  # プロパティの追加
    orientation='vertical'
    def __init__(self, **kwargs): #クラス初期化
        super().__init__(**kwargs)
        
        
        response = get_htmls('6758')
       #Label(font_name='/path/font/meiryo.ttc', text='はろーワールド')
        btn = Label(text=str(get_htmls('4755')))
        print(response)
        self.add_widget(btn)

        btn2 = Button(text="毎日")
        self.add_widget(btn2)

        # MainScreenに追加する、BoxLayoutというWidgetを用意
        bl = BoxLayout()
        bl.orientation = "vertical"#horizontal 

        # blに追加する３つのボタンを用意
        btn3 = Button(text="how")
        btn4 = Button(text="are")
        btn5 = Button(text="you")

        # blにボタンを追加
        bl.add_widget(btn3)
        bl.add_widget(btn4)
        bl.add_widget(btn5)

        # MainScreenにblを追加
        self.add_widget(bl)

        btn6 = Button(text="today?")
        self.add_widget(btn6)


class MyApp(App): #アプリケーションのロジックを記述するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Python Ios App'  # ウィンドウの名前を変更
       

    def on_start(self):
        print("App Start!!")

    def build(self):
        MS = MainScreen()
        return MS

    def on_stop(self):
        print("App End!!")

    #def build(self):
        #s = ScatterPlane(scale=1.0)
       
        #b1 = MainScreen()
        #highs = get_Year_to_date_highs()
        #volume = Volume_per_unit()
        #price = Price_drop()
        #stop = Stop_High()
        #only = Only_Price()
        #post= Posted_version()
        
        #s.add_widget(highs)
        #s.add_widget(b1)
        #s.add_widget(l1)
        #s.add_widget(l2)
        #return s
        #return SampleScreen()
class MainScreen(Widget):
    text = StringProperty()    # プロパティの追加
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.text = '99999999999'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked(self):        # ボタンをクリック時
        self.text = 'Hello PythonWorld'
        self.color = [0, 1, 0 , 1 ]

    def geturlClicked(self):        # ボタンをクリック時
        #self.text = 'Get Url'
        self.text = str(get_htmls('6758'))
        self.color = [0, 1, 0 , 1 ]


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'Python to IosApp'

    def on_start(self):
        stack_code = ['998407','6758', '6976', '4755']
        data1 = ''
        print("App Start!!")

    def build(self):
        MS = MainScreen()
        return MS

    def on_stop(self):
        print("App End!!")
    

    #def build(self):
    #    return MainScreen()

if __name__ == '__main__':
    TestApp().run()