from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SampleScreen(BoxLayout): #ユーザーインタフェースを記述するクラス
    def __init__(self, **kwargs): #クラス初期化
        super().__init__(**kwargs)
        self.add_widget(Button(text="Hello Python World"))


class SampleApp(App): #アプリケーションのロジックを記述するクラス
    def build(self):
        return SampleScreen()


SampleApp().run()