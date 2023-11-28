import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder 
from kivy.app import App
from kivy.graphics import Canvas
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file('design-optimize2.kv')


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):
        self.name=self.ids.name.text
        self.say=Label(
            text=f'hello {self.name}',
            pos_hint={'center_x':0.3,'y':0},
            size_hint=(0.4,0.4)
        )
        return self.ids.warp.add_widget(self.say)
    def clear(self):
        self.ids.name.text=''
        self.say.text=''
    def next(self):
        self.manager.current='congrats'

class play(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class app(App):
    def build(self):
        self.manage=ScreenManager()
        self.manage.add_widget(main(name='log'))
        self.manage.add_widget(play(name='congrats'))
        return self.manage
if __name__=='__main__':
    app().run()