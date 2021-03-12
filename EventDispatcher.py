from kivy.event import EventDispatcher
from kivy.properties import StringProperty, NumericProperty


class Person(EventDispatcher):

    name = StringProperty()
    age = NumericProperty()

    def on_name(self, __, value):
        print(f'nameの値が{value}に書き換えられました')

    def on_age(self, __, value):
        print(f'ageの値が{value}に書き換えられました')    


person = Person(name='Bob', age=20)#インスタンス
#person.bind(age=lambda __, value: print(f'ageの値が{value}に書き換えられました'))
print('--------')
person.name = 'Ema'
person.age = 30