from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


class EvevtTestApp(App):
    def build(self):
        self.title = 'Hello'
       

    def add_more(self):
        print('Add-test')
        addbutton = self.root.ids.mainscreen.ids.abc
        addbutton.add_widget(Button(text='hello'))

    def remove(self):
        print('Remove-test')
        container = self.root.ids.mainscreen.ids.abc
        if len(container.children) > 0:
            container.remove_widget(container.children[0])



if __name__=='__main__':
    EvevtTestApp().run()