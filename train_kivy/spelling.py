import kivy
kivy.require('2.1.0')
from kivy.core.spelling import Spelling
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self):
        s=Spelling()
        word=self.ids.word.text
        s.select_language('en_US')
        option= s.suggest(word)
        x=''
        for i in option:
            x=f'{x} \n {i}'
        self.ids.label1.text=x

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('spelling.kv')
    
    def build(self):
        self.screenmanager=ScreenManager()
        self.screenmanager.add_widget(main(name='main'))
        return self.screenmanager

if __name__=='__main__':
    app().run()