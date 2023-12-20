import kivy
kivy.require('2.2.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def slide(self,*args):
        self.ids.word.text=str(int(args[1]))
        self.ids.word.font_size=str(int(args[1])*5)

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('slide.kv')
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(main(name='main'))
        return self.sm
    
if __name__=='__main__':
    app().run()

