from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scatter import ScatterPlane
from kivy.uix.label import Label
from bs4 import BeautifulSoup
import requests

class get_Year_to_date_highs(BoxLayout):
    def __init__(self, **kwargs): #クラス初期化
        super().__init__(**kwargs)

        urlName ='https://info.finance.yahoo.co.jp/ranking/?kd=29&mk=3&tm=d&vl=a'#年初来高値
        soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
        text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
        data1 = [d.text for d in soup.find_all('td')]
        #for i in range(1, len(data1)):
        #  print('年初来高値: '.decode('utf-8')+data1[i])
        self.add_widget(Button(text= 'data1',font_size=98, pos=(400, 100)))

  

class SampleScreen(BoxLayout): #ユーザーインタフェースを記述するクラス
    def __init__(self, **kwargs): #クラス初期化
        super().__init__(**kwargs)
        self.add_widget(Button(text="Hello Python",font_size=30, pos=(400, 100)))


class SampleApp(App): #アプリケーションのロジックを記述するクラス
    def build(self):
        s = ScatterPlane(scale=.5)
        l1 = Label(text='Kivy rulz', font_size=98, pos=(400, 100), mipmap=True)
        l2 = Label(text='Kivy rulz', font_size=98, pos=(400, 328))
        b1 = SampleScreen()
        highs = get_Year_to_date_highs()
        #volume = Volume_per_unit()
        #price = Price_drop()
        #stop = Stop_High()
        #only = Only_Price()
        #post= Posted_version()
        
        s.add_widget(highs)
        s.add_widget(b1)
        s.add_widget(l1)
        s.add_widget(l2)
        return s
        #return SampleScreen()

if __name__ == '__main__':
    SampleApp().run()