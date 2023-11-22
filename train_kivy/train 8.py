import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
Builder.load_file('train 8.kv')

class GUI(FloatLayout):
    def __init__(self, **kwargs):
        super(GUI,self).__init__(**kwargs)
        self.pos_x= 0.5
        self.pos_y= 0.75
        self.obj = self.ids.obj2
    def r_move(self):
        self.pos_x +=0.01
        anim= Animation(pos_hint={'x': self.pos_x, 'y': self.pos_y},duration=0.1)
        anim.start(self.obj)
    def l_move(self):
        self.pos_x -=0.01
        anim= Animation(pos_hint={'x': self.pos_x, 'y': self.pos_y},duration=0.1)
        anim.start(self.obj)
    def u_move(self):
        self.pos_y += 0.01
        anim= Animation(pos_hint={'x': self.pos_x, 'y': self.pos_y},duration=0.1)
        anim.start(self.obj)
    def d_move(self):
        anim= Animation(pos_hint={'x': self.pos_x, 'y': self.pos_y},duration=0.1)
        self.pos_y -=0.01
        anim.start(self.obj)


class app(App):
    def build(self):
        return GUI()

if __name__== '__main__':
    app().run()