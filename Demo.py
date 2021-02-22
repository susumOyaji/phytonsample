from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (500, 400)

class User(Screen):

    def add_more(self):
        self.ids.rows.add_row()


class Row(BoxLayout):
    button_text = StringProperty("")


class Rows(BoxLayout):
    row_count = 0

    def __init__(self, **kwargs):
        super(Rows, self).__init__(**kwargs)
        self.add_row()

    def add_row(self):
        self.row_count += 1
        self.add_widget(Row(button_text=str(self.row_count)))


class Test1(App):

    def build(self):
        self.root = Builder.load_file('Demo.kv')
        return self.root


if __name__ == '__main__':
    Test1().run()