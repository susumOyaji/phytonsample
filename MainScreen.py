# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
#import japanize_kivy

kv = """
#:import hex kivy.utils.get_color_from_hex
<MainScreen>:
    BoxLayout: #All-Screen
        orientation: 'vertical'
        rv: rv
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
    RecycleView:
        id: rv
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: sp(60) #スクロール速度
        bar_width: sp(20)
        viewclass: 'VariousButtons'
        RecycleBoxLayout:
            default_size: None, sp(160)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(8)
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

class VariousButtons(BoxLayout):
    def on_select_button(self, button):
        print('pressaaa:' + button.text)        
       

if __name__=="__main__":
    MainApp().run()