# coding:utf-8
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from bs4 import BeautifulSoup
import requests
#import japanize_kivy
from kivy.config import Config  # 追加


Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '650')  # 追加
Config.set('graphics', 'height', '1350')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1400)
Config.set('graphics', 'top', 35)


#企業コード nikkei,sony,taiyou,rukten
code = ['6758', '6976', '4755'] 
price = [1665, 1801, 1137] #購入単価
quantity = [200, 300, 400] #数量
Marketprice = [] #個別時価総額=数量ｘ時価
value = [] #時価
name = [] #企業名
before = []
ratio = []
TotalValue = 0



kv = """
#:import hex kivy.utils.get_color_from_hex
<MainScreen>:
    rv: rv
    BoxLayout: #All-Screen
        orientation: 'vertical'
        #size_hint_y: 1.0
        canvas.before:
            Color:
                rgba: hex('#ffffff')
            Line:
                rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                dash_offset: 5
                dash_length: 3
            #Rectangle:
            #    pos: self.pos
            #    size: self.size
        BoxLayout: #Stack-Card
            #orientation: 'horizontal'
            size_hint_y: 0.3
            canvas.before:
                Color:
                    rgba: hex('#fc0317')
                Line:
                    rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                    dash_offset: 5
                    dash_length: 3
            Label:
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                text: 'Stock-Card'
                pos_hint:{ 'center_x': .5,'center_y': .5}
                size_hint_y: 0.6
                size_hint_x: 0.8
                color: 1, 0, 0, 1 #text color
                bold: True
                font_size: 60
                spacing: 0.0, 0.0#    
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                        dash_offset: 5
                        dash_length: 3
                    #Rectangle:
                    #    pos: self.pos
                    #    size: self.size
            Button:
                text:'Button'
                size_hint_y: 0.3
                size_hint_x: 0.1
                pos_hint:{ 'center_x': .5,'center_y': .5}
                canvas.before:
                    Color:
                        rgba: hex('#ffffff')
                    Line:
                        rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                        dash_offset: 5
                        dash_length: 3
                    #Rectangle:
                    #    pos: self.pos
                    #    size: self.size

        BoxLayout:
            #orientation: 'vertical'
            size_hint_y: 0.3
            canvas.before:
                Color:
                    rgba: hex('#fc0317')
                Line:
                    rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                    dash_offset: 5
                    dash_length: 3
            Label:
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                text: 'NewYork Dow'
                size_hint_y: 0.5
                size_hint_x: 1.0
                pos_hint:{ 'center_x': .5,'center_y': .5}
                #padding: 0.0, 25.0 #左右、上
                #spacing: 0.0, 0.0#       
                color: 1, 0, 0, 1#text color
                bold: True
                font_size: 50
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                        dash_offset: 5
                        dash_length: 3
                    #Rectangle:
                    #    pos: self.pos
                    #    size: self.size
        BoxLayout:
            #orientation: 'vertical'
            size_hint_y: 0.3
            canvas.before:
                Color:
                    rgba: hex('#fc0317')
                Line:
                    rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                    dash_offset: 5
                    dash_length: 3
            Label:
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                text: 'Nikkei225'
                size_hint_y: 0.5
                size_hint_x: 0.8
                pos_hint:{ 'center_x': .5,'center_y': .5}
                color: 1, 0, 0, 1#text color
                bold: True
                font_size: 30
                spacing: 0.0, 0.0#    
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                        dash_offset: 5
                        dash_length: 3
                    #Rectangle:
                    #    pos: self.pos
                    #    size: self.size      
    #rv: rv
    Widget:
        id: separator
        size_hint_y: None
        height: 20
        canvas:
            Color:
                rgb: 1., 1., 0.
            Rectangle:
                pos: 0, separator.center_y
                size: separator.width, 5
    RecycleView:
        id: rv
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: sp(60) #スクロール速度
        bar_width: sp(20)
        viewclass: 'VariousButtons'
        RecycleBoxLayout:
            default_size: None, sp(90) #Higth
            default_size_hint: 1.0, None #width
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(10)
<VariousButtons>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value: ''
    Button:
        text: root.value
        background_normal: ''
        background_color: 0.5, 0.5, 0.75, 1
        color: 1, 1 ,1 ,1
        on_press: root.on_select_button(self)
        
"""
Builder.load_string(kv)

def get_htmls(stock_number):
  data = []

  urlName = "https://finance.yahoo.co.jp/quote/"+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  #text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  tag_tr = soup.find_all('body')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('span')]
  name = [h.text for h in tag_tr[0].find_all('h1')]
  #print(head[0])#ソニー（株）
   
  data.append(name[1])
  data.append(head[22])
  data.append(head[29])
 
  print('Name: ',data[0])
  print('StoksPrice: ',data[1])
  print('The day before ratio: ',data[2])
  print('')
  return data



def get_dowhtmls():
  urlName = 'https://finance.yahoo.co.jp/quote/%5EDJI'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('dd')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[3].find_all('span')]#th
  data = head[0]
  return data



def get_nikkeyhtmls():
  data = []  
  #urlName = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
  urlName = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('body')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[0].find_all('td')]  #tr
  
  value = head[1]
  ratio = head[2]
  name = head[3]
  
  data.append(name)
  data.append(value)
  data.append(ratio)
  return data


def get_htmls(stock_number):
  data = []

  urlName = "https://finance.yahoo.co.jp/quote/"+stock_number
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  #text=soup.get_text()#.get_text()は、テキストのみを取得する、つまりタグは取らないメソッドです。
  
  tag_tr = soup.find_all('body')
  #print(tag_tr[0])

  head = [h.text for h in tag_tr[0].find_all('span')]
  name = [h.text for h in tag_tr[0].find_all('h1')]
  #print(head[0])#ソニー（株）
   
  data.append(name[1])
  data.append(head[22])
  data.append(head[29])
 
  print('Name: ',data[0])
  print('StoksPrice: ',data[1])
  print('The day before ratio: ',data[2])
  print('')
  return data


class MainScreen(BoxLayout):#画面上の見た目や機能を構成するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"#horizontal"
        self.rv.data = []
                  
        for name_list_any in name:
            self.rv.data.append({'value': name_list_any})

    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        value.append(responce[1])
        ratio = responce[2].replace('前日比','')
        before.append(ratio)        
    #Newyork dow
    dow = get_dowhtmls()
    #Label2
    newyork = 'NewYork Dow $' + dow
    #Nikkei25
    nikkei= get_nikkeyhtmls()
    #Label3
    nikei225 = nikkei[0] + nikkei[1] + '\n' + nikkei[2]
    
    for i in range(len(code)):
        try:
            Marketprice.append(float(value[i].replace(',', '')) * quantity[i])
            TotalValue = TotalValue + Marketprice[i]
        except ValueError:
            Marketprice.append('---')
        
    #Label4
    TotalAsset= 'TotalAsset   ¥'+str("{:,}".format(TotalValue))    
        
'''
btn = Button(text="hello")
self.add_widget(btn)

btn2 = Button(text="everyone")
self.add_widget(btn2)


# MainScreenに追加する、BoxLayoutというWidgetを用意
bl = BoxLayout()
bl.orientation = "vertical"

# blに追加する３つのボタンを用意
lbl3 = Label(text="how")
lbl3.size_hint_y = 0.5
lbl3.size_hint_x = 0.5
lbl3.color = 1, 0, 0, 1#text color
lbl3.bold = True
lbl3.font_size = 30
lbl3.bg='#F0F8FF'
# 色を設定
#lbl3['bg'] = '#F0F8FF'
#lbl3.config(bg='#F0F8FF')


lbl4 = Label(text="are")
lbl5 = Label(text="you")

# blにボタンを追加
bl.add_widget(lbl3)     
bl.add_widget(lbl4)
bl.add_widget(lbl5)

# MainScreenにblを追加
self.add_widget(bl)

btn6 = Button(text="today?")
self.add_widget(btn6)
'''

class MainApp(App):#アプリを構成するクラス
    def on_start(self):
        print("App Start!!")

    def build(self):
        MS = MainScreen()
        self.title = 'Python to Iphone App'
        return MS

    def on_stop(self):
        print("App End!!")

class VariousButtons(BoxLayout):
    def on_select_button(self, button):
        print('pressaaa:' + button.text)        
       

if __name__=="__main__":
    MainApp().run()