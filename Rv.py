#(main.py)


import re#正規表現

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout


class AppRoot(BoxLayout):
    pat = re.compile(r'\.{3}')
    my_rv = ObjectProperty()

    def choose_data(self, btn):
        print(f"Index {btn.index}: {btn.text}")

    def create_data(self, btn):
        data_txt = self.pat.sub(self.ids.input.text.capitalize(), btn.text)
        self.my_rv.data.append({'text': data_txt})  # 2:


class MyRecycleBoxLayout(RecycleBoxLayout):
    def add_widget(self, widget, index=0, canvas=None):  # 4:
        widget.index = self.view_indices[widget]  # 6:
        if widget.index % 2:
            widget.background_color = 0, 0, 1, 0.5
        else:
            widget.background_color = 1, 0, 0, 0.5
        super().add_widget(widget, index, canvas)  # 5:


class RVApp(App):
    pass


if __name__ == '__main__':
    RVApp().run()
