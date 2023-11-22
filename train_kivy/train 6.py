import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
Builder.load_file('train 6.kv')

class analog(FloatLayout):
    def __init__(self,**kwargs):
        super(analog,self).__init__(**kwargs)
        self.pos_hint_x=0
        self.pos_hint_y=0.5
    def move_r (self):
        sq=self.ids.obj2
        self.pos_hint_x+=0.01
        anim= Animation(pos_hint={'x':self.pos_hint_x,'y':self.pos_hint_y},duration=0.1)
        anim.start(sq)

class app(App):
    def build(self):
        return analog()
if __name__=='__main__':
    app().run()