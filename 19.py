from random import sample
from string import ascii_lowercase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
import japanize_kivy
from kivy.config import Config  # 追加
from bs4 import BeautifulSoup
import requests


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
TotalAsset=0

# 日本語フォント設定
resource_add_path('./fonts')
#LabelBase.register(DEFAULT_FONT, 'ipaexg.ttf')





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
  head = [h.text for h in tag_tr[0].find_all('tr')]  #tr
 
  s = head[0]
  name = s[1:7]  # スライスで半角空白文字よりも前を抽出
  
  target = "\n前"
  idx = s.find(target)
  stock = s[12:idx]
  
  target = " \n"
  idx = s.find(target)
  ratio = s[16:idx]

  data.append(name)
  data.append(stock)
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
  #print(head[0])#ソニー（株）
  s = head[81]
  target = "の"
  idx = s.find(target)
  r = s[:idx]  # スライスで半角空白文字よりも前を抽出

 
  data.append(r+head[17])
  data.append(head[22])
  data.append(head[29])
 
  print('Name: ',data[0])
  print('StoksPrice: ',data[1])
  print('The day before ratio: ',data[2])
  print('')
  return data

kv = """
<MyuserLabel@Label>:
    pos_hint_y: None
    font_size: 5
    font_name: 'Verdana'


<SmoothButton@Button>:
    background_color:(0,0,0,0)
    background_normal:''
    back_color: (0.565, 0.557, 0.698,0.8)
    border_radius:[0,35,0,35]
    #font_name:'verdana'
    canvas.before:
        Color:
            rgba:self.back_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.border_radius
<VariousButtons>:
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value: ''
    Button:
        size_hint_y: 1
        text: root.value
        background_normal: ''
        background_color: 0.5, 0.5, 0.75, 1
        color: 1, 1 ,1 ,1
        on_press: root.on_select_button(self)
<Test>:
    orientation: 'vertical'
    rv: rv
    BoxLayout: #All Screen
        orientation: "vertical"
        canvas:
            Color:
                rgba: 1, 0.3, 0.3, 1
            Rectangle:
                size: self.size
                pos: self.pos
        BoxLayout:#Stack Card
            orientation: "vertical"
            canvas:
                Color:
                    rgba: 0.3, 0.3, 0.3, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
        #rv: rv
        RecycleView:
            id: rv
            scroll_type: ['bars', 'content']
            scroll_wheel_distance: sp(60) #スクロール速度
            bar_width: sp(20)
            viewclass: 'VariousButtons'
            RecycleBoxLayout:
                default_size: None, sp(100)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                spacing: dp(8)
"""
Builder.load_string(kv)








class TextWidget(BoxLayout):
    pass

class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.rv.data = []
        TotalValue = 0


        for i in code:
            responce = get_htmls(i)
            name.append(responce[0])
            value.append(responce[1])
            #before.append(responce[2]) #前日比
            ratio = responce[2].replace('前日比','')
            before.append(ratio)
        

        #Newyork dow
        dow = get_dowhtmls()
        #Label2
        newyork = 'NewYork Dow $' + dow
        #Nikkei25
        nikkei= get_nikkeyhtmls()
        #Label3
        nikei225 = nikkei[0] + nikkei[1] + '\n'+  nikkei[2]
        btn_list=[]
        value_list=[]
        for i in range(len(code)):
            try:
                btn_list.append(name[i])
                value_list.append(value[i])

                Marketprice.append(float(value[i].replace(',', '')) * quantity[i])
                TotalValue = TotalValue + Marketprice[i]
            except ValueError:
                Marketprice.append('---')
        
        #Label4
        TotalAsset= 'TotalAsset   ¥'+str("{:,}".format(TotalValue))

        for btn_list_any in btn_list:
            self.rv.data.append({'value': btn_list_any})


            
class VariousButtons(BoxLayout):
    def on_select_button(self, button):
        print('press:' + button.text)
        print('Id:' + str(self.ids.values))
        
class TestApp(App):
    def build(self):
        return Test()

        
if __name__ == '__main__':
    TestApp().run()