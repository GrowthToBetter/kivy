import kivy 
kivy.require('2.1.0')
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Color,Rectangle
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
Builder.load_file('train 7.kv')

class rlayout(RelativeLayout):
    def __init__(self, **kw):
        super(rlayout,self).__init__(**kw)
        self.pos_x=0.5
        self.pos_y=0.75
        self.mobject=self.ids.mobject
    def r_move(self):
        self.pos_x += 0.1
        anim= Animation(pos_hint={'center_x': self.pos_x, 'center_y': self.pos_y}, duration=0.01)
        anim.start(self.mobject)
    def l_move(self):
        self.pos_x -=0.1
        anim= Animation(pos_hint={'center_x': self.pos_x, 'center_y': self.pos_y}, duration=0.01)
        anim.start(self.mobject)
    def u_move(self):
        self.pos_y +=0.1
        anim= Animation(pos_hint={'center_x': self.pos_x, 'center_y': self.pos_y}, duration=0.01)
        anim.start(self.mobject)
    def d_move(self):
        self.pos_y -=0.1
        anim= Animation(pos_hint={'center_x': self.pos_x, 'center_y': self.pos_y}, duration=0.01)
        anim.start(self.mobject)
class app(App):
    def build(self):
        return rlayout()     

if __name__=='__main__':
    app().run()