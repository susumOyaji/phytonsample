from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
#from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
import japanize_kivy
from kivy.uix.button import Button
import time
import datetime
import threading
from kivy.event import EventDispatcher
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#######
from kivy.config import Config  # 追加
from bs4 import BeautifulSoup
import requests
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '800')  # 追加
Config.set('graphics', 'height', '1350')  # 追加
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1300)
Config.set('graphics', 'top', 35)

# Path of Fonts
#resource_add_path('/usr/share/fonts/truetype/takao-gothic')
#LabelBase.register(DEFAULT_FONT, 'TakaoGothic.ttf')  # 日本語が使用できるように日本語フォントを指定する


#Window.clearcolor = (0.5, 0.5, 0.5, 1)
#Window.size = (900, 1320)

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


def get_dowhtmls():
  urlName = 'https://finance.yahoo.co.jp/quote/%5EDJI'
  soup = BeautifulSoup(requests.get(urlName).content, 'html.parser')
  
  tag_tr = soup.find_all('dd')#tr
  #print(tag_tr[0])
  head = [h.text for h in tag_tr[3].find_all('span')]#th
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
    item_ratio = StringProperty("")






class Rows(BoxLayout):
    row_count = 0
    

#一定時間ごとに繰り返し
#スレッドがスレッドを起動するようにしておくと、一定時間ごとに繰り返すようにできる。
#この例では１秒ごとにheloheloをprintする。これは何かに役立つかもしれない
    '''
    import threading
 
    def hello():
        print "helohelo"
        t=threading.Timer(1,hello)
        t.start()
    t=threading.Thread(target=hello)
    t.start()
    '''


    
    #while False:
    for i in code:
        responce = get_htmls(i)
        name.append(responce[0])
        value.append(responce[1])
        #before.append(responce[2]) #前日比
        ratio = responce[2].replace('前日比','')
        before.append(ratio)    
    #time.sleep(10)


    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
    # self.row_count = 0
        self.add_code()
        
    def add_row(self):
        self.row_count += 1
        self.add_widget(Row(button_text=str(self.row_count),item_value=str(self.row_count)))


    def add_code(self):
        for i in code:
            responce = get_htmls(i)
            name.append(responce[0])
            value.append(responce[1])
            #before.append(responce[2]) #前日比
            ratio = responce[2].replace('前日比','')
            before.append(ratio)    


        for i in range(len(code)):
            self.row_count += 1
            self.add_widget(Row(button_text=str(self.row_count),item_value=name[i]+'\n'+ value[i],item_ratio= before[i]))
    
    def Referencing_Widgets(self):
        self.row_count = 0
        name=[];value=[]
        for i in code:
            responce = get_htmls(i)
            name.append(responce[0])
            value.append(responce[1])
            #before.append(responce[2]) #前日比
            ratio = responce[2].replace('前日比','')
            before.append(ratio)
            button_text=str(self.row_count)    
            item_value = value[self.row_count]
            self.row_count += 1
    #event = Clock.schedule_interval(my_callback, 1 / 30.)
           



'''
    def remove_row(self):
        if self.content.children:
            self.content.remove_widget(self.content.children[0])
            self.row_count -= 1
'''





'''
KvLanguageのclass ruleとroot ruleの違いを説明させて下さい。
まずclass rule("<クラス名>:"で始まるもの)は
型の定義であり、そこに書いた物はその型のインスタンス全てに影響を与えます(厳密には少し違いますが)。
そしてclass ruleを書いただけではインスタンスは作られません

それに対してroot rule("クラス名:"で始まるもの)は
書いただけでインスタンスが一つ作られ、それがBuilder.load_string()の戻り値になります。
そしてroot ruleに書いた様々な定義はそのインスタンスのみの物で、他のインスタンスには影響を与えません。
'''


class user(Screen):
    
    def add_more(self):#Add Button to Push
        self.ids.rows.add_row()

    def data_update(self):
        self.ids.rows.Referencing_Widgets()


    #Newyork dow
    dow = get_dowhtmls()
    #Label2
    newyork = 'NewYork Dow $' + dow
    #Nikkei25
    nikkei= get_htmls('998407')
    #Label3
    nikei225 = nikkei[0] + '   ¥' + nikkei[1] #+ '\n¥' + str(Marketprice[0])
    

    for i in range(len(code)):
        try:
            Marketprice.append(float(value[i].replace(',', '')) * quantity[i])
            TotalValue = TotalValue + Marketprice[i]
        except ValueError:
            Marketprice.append('---'); newyork = '---'; nikei225 = '---'
        
    #Label4
    TotalAsset= 'TotalAsset   ¥'+str("{:,}".format(TotalValue))
    
    
    
   


    
                 


class Test1(App):
    def build(self):
        #self.root = Builder.load_file('Demo.kv')
        self.root = Builder.load_file('floatlayout.kv')
        self.title = 'Python to Iphone App'
        return self.root




if __name__ == '__main__':
    Test1().run()