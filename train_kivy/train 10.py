



import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
 
Builder.load_file('train 10.kv')
class floatla(FloatLayout):
    def __init__(self, **kwargs):
        super(floatla,self).__init__(**kwargs)
    def open(self):
        pop().open()
class pop(Popup):
    def __init__(self, **kwargs):
        super(pop,self).__init__(**kwargs)
    def close(self):
        self.dismiss()

class app(App):
    def build(self):
        return floatla()

if __name__=='__main__':
    app().run()



