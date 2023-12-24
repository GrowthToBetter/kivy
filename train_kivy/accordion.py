import kivy
kivy.require('2.2.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('accordion.kv')
    
    def build(self):
        sm= ScreenManager()
        sm.add_widget(main(name='main'))
        return sm

if __name__ =='__main__':
    app().run()