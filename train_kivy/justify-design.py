import kivy
kivy.require('2.1.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Canvas, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App
from kivy.animation import Animation

Builder.load_file('justify-design.kv')
class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def press(self):
        self.name=self.ids.name.text
        self.alert=Label(
            text=f'welcome back {self.name}',
            size_hint=(0.6,0.4),
            font_size=25,
            pos_hint={'center_x':0.3,'y':0},
        )
        return self.ids.warp.add_widget(self.alert)
    
    def reset(self):
        self.ids.name.text=''
        self.alert.text=''

    
    def next(self):
        self.manager.current='play'

class play(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.thing=self.ids.Box
        self.pos_x=self.thing.x
        self.pos_y=self.thing.y
        
    def click(self):
        if self.pos_x>=0.9 :
            self.pos_x=-0.1
            self.manager.current='win'
        # if self.pos_y>=0.9:
        #     self.pos_y=-0.1
        
        self.pos_x +=0.1
        animation= Animation(duration=0.001,
                             pos_hint={'x':self.pos_x,'y':self.pos_y})
        return animation.start(self.thing)

class win(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class app(App):
    def build(self):
        self.manage=ScreenManager()
        self.manage.add_widget(main(name='main'))
        self.manage.add_widget(play(name='play'))
        self.manage.add_widget(win(name='win'))
        return self.manage

if __name__=='__main__':
    app().run()