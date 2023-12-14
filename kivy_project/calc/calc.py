import kivy
kivy.require('2.1.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivy.core.window import Window

Window.size=(500,700)


Builder.load_file('calc.kv')
class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self):
        self.name=self.ids.name.text
        self.password=self.ids.password.text
        self.animation=Animation(duration=0.5, opacity=1)+Animation(duration=1,opacity=0)
        if self.name =='bara' and self.password=='1':
            self.manager.current='calc'
            self.ids.name.text=''
            self.ids.password.text=''
            self.manager.get_screen('calc').ids.logged.opacity=1
            self.animation.start(self.manager.get_screen('calc').ids.logged)
        else:
            self.ids.name.text=''
            self.ids.password.text=''
            self.ids.incorrect.opacity=1
            animation=Animation(duration=1,opacity=0)
            animation.start(self.ids.incorrect)
    
class calc(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self,button):
        self.prior=self.ids.show
        if 'Unknown' in self.prior.text:
            self.ids.show.text=''
        if self.prior.text=='0' :
            self.ids.show.text=f'{button}'
        else:
            self.ids.show.text=f'{self.prior.text}{button}'
    def clear(self,type):
        if type==1:
            self.ids.show.text=''
        if type==2:
            self.ids.show.text=f'{self.ids.show.text[:-1]}'
    def sign_math(self,sign):
        self.sign=sign
        self.ids.show.text=f'{self.prior.text}{self.sign}'
    def dec(self):
        sign=['*','/','+','-']
        if '.' not in self.ids.show.text:
            self.ids.show.text=f'{self.ids.show.text}.'
        for i in sign:
            if i in self.ids.show.text:
                list_number=self.ids.show.text.split(i)
                print(list_number)
                if i in self.ids.show.text and '.' not in list_number[-1]:
                    self.ids.show.text=f'{self.ids.show.text}.'
                    break
            else:
                continue
        
        
    def negativity(self):
        if '-' in self.ids.show.text:
            self.ids.show.text=f"{self.ids.show.text.replace('-','')}"
        else:
            self.ids.show.text=f"-{self.ids.show.text}"
    def equal(self):
        prior=self.prior.text
        if prior=='3347':
            self.manager.current='hide'
        else:
            try:
                result=eval(self.ids.show.text)
                self.ids.show.text=str(result)
            except:
                self.ids.show.text='Unknown'

class hide(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class app(App):
    def build(self):
        self.screen_manage=ScreenManager()
        self.screen_manage.add_widget(main(name='main'))
        self.screen_manage.add_widget(calc(name='calc'))
        self.screen_manage.add_widget(hide(name='hide'))
        return self.screen_manage
    
if __name__=='__main__':
    app().run()