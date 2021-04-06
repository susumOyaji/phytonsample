# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

kv = """
#:import hex kivy.utils.get_color_from_hex
<MainScreen>:
    BoxLayout: #All-Screen
        orientation: 'vertical'
        size_hint_y: 0.3
        canvas.before:
            Color:
                rgba: hex('#ff0606')
            Line:
                rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                dash_offset: 5
                dash_length: 3
            #Rectangle:
            #    pos: self.pos
            #    size: self.size
        BoxLayout: #Stack-Card
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: hex('#ffff06')
                Line:
                    rectangle: self.x+1,self.y+1,self.width-1,self.height-1
                    dash_offset: 5
                    dash_length: 3
            Label:
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                pos_hint:{ 'center_x': .5,'center_y': .8}
                #padding: 50.0,50.0 #左右、上下
                #spacing: 50.0,50.0 #pixcel        
                text: 'Stock Card'
                #size_hint_y: None
                size_hint_y: 0.3
                size_hint_x: 0.5
                color: 1, 0, 0, 1#text color
                bold: True
                font_size: 30
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
            orientation: 'vertical'
            size_hint_y: 0.3
            Label:
                text: 'Label 2'
                size_hint_y: 0.3
                size_hint_x: 1.0
                pos_hint:{ 'center_x': .5,'center_y': .5}
                #padding: 0.0, 25.0 #左右、上
                spacing: 150.0, 150.0#       
                color: 1, 0, 0, 1#text color
                bold: True
                font_size: 30
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
            orientation: 'vertical'
            size_hint_y: 0.3
            Label:
                text: 'Label 3'
                size_hint_y: 0.3
                size_hint_x: 0.8
                color: 1, 0, 0, 1#text color
                bold: True
                font_size: 30
                spacing: 150.0, 150.0#    
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

        
"""
Builder.load_string(kv)


class MainScreen(BoxLayout):#画面上の見た目や機能を構成するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        self.orientation = "vertical"#horizontal"
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
        return MS

    def on_stop(self):
        print("App End!!")
       

if __name__=="__main__":
    MainApp().run()