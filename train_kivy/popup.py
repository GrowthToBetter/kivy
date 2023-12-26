import kivy
kivy.require('2.2.1')
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def open(self):
        pop().open()

class pop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def close(self): 
    #     self.dismiss()  jika auto dismiss false, maka harus menggunakan function
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('popup.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm

if __name__=='__main__':
    app().run()