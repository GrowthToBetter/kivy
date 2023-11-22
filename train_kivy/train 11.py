import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Color,Rectangle
from kivy.animation import Animation




Builder.load_file('train 11.kv')


class main(FloatLayout):
    def __init__(self, **kwargs):
        super(main,self).__init__(**kwargs)
    
    def open(self):
        in_popup=pop()
        in_popup.open()

class pop(Popup):
    def __init__(self, **kwargs):
        super(pop,self).__init__(**kwargs)
        self.my_player= self.ids.player
        self.pos_x=0.3
        self.pos_y=0.7
    def rM(self):
        self.pos_x+=0.01
        anim= Animation(pos_hint={'x': self.pos_x,'y': self.pos_y},duration=0.01)
        anim.start(self.my_player)
    def lM(self):
        self.pos_x-=0.01
        anim= Animation(pos_hint={'x': self.pos_x,'y': self.pos_y},duration=0.01)
        anim.start(self.my_player)
    def uM(self):
        self.pos_y+=0.01
        anim= Animation(pos_hint={'x': self.pos_x,'y': self.pos_y},duration=0.01)
        anim.start(self.my_player)
    def dM(self):
        self.pos_y-=0.01
        anim= Animation(pos_hint={'x': self.pos_x,'y': self.pos_y},duration=0.01)
        anim.start(self.my_player)
    def close(self):
        self.dismiss()

class app(App):
    def build(self):
        return main()

if __name__=='__main__':
    app().run()