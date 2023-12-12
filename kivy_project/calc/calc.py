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

Builder.load_file('calc.kv')
class main(Screen):
    mode='main'
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
        if self.prior.text=='0' :
            self.ids.show.text=f'{button}'
        else:
            self.ids.show.text=f'{self.prior.text}{button}'
    def clear(self):
        self.ids.show.text='0'
    def plus(self):
        self.ids.show.text=f'{self.prior.text}+'
    def min(self):
        self.ids.show.text=f'{self.prior.text}-'
    def divide(self):
        self.ids.show.text=f'{self.prior.text}/'
    def multiple(self):
        self.ids.show.text=f'{self.prior.text}x'
    def equal(self):
        prior=self.prior.text
        result=0
        result_2=1
        if '+' in prior:
            num= prior.split('+')
            for number in num:
                result+= int(number)
            self.prior.text=str(result)
        if '-' in prior:
            num= prior.split('-')
            for number in num:
                result-= int(number)
            self.prior.text=str(result)
        if '/' in prior:
            num= prior.split('/')
            for number in num:
                result_2 /= int(number)
            self.prior.text=str(result_2)
        if 'x' in prior:
            num= prior.split('x')
            for number in num:
                result_2 *= int(number)
            self.prior.text=str(result_2)


class app(App):
    def build(self):
        self.screen_manage=ScreenManager()
        self.screen_manage.add_widget(main(name='main'))
        self.screen_manage.add_widget(calc(name='calc'))
        return self.screen_manage
    
if __name__=='__main__':
    app().run()