import kivy
kivy.require('2.2.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self, value):
        if value=='Emilia' or value=='Elaina':
            self.ids.alert.text= f'i love {value} too'
        else:
            self.ids.alert.text=f'i hate you'
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('dropdownspinner.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm
if __name__=='__main__':
    app().run()