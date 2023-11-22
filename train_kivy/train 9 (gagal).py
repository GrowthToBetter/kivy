from typing import Any
import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
Builder.load_file('train 9.kv')
from kivy.uix.button import Button
from kivy.uix.label import Label



class main(BoxLayout):
    def __init__(self, **kwargs):
        super(main,self).__init__(**kwargs)
    def open(self):
        print('succes')
        this_popup().open()

class this_popup(Popup):
    def close(self):
        self.dismiss()

class MainApp(App):
    def build(self):
        return main()
    
if __name__=='__main__':
    MainApp().run()