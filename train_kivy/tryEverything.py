import kivy
kivy.require('2.2.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Canvas, Rectangle, RoundedRectangle
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.spelling import Spelling
from kivy.uix.filechooser import FileChooserIconView
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import *
from kivy.core.window import Window
Window.size=(350,700)



class login(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self):
        self.animation_login()
        self.manager.current='main'
        self.manager.transition= WipeTransition()
        with open('../tryEverything.txt','w') as file:
            file.write(f'{self.ids.name.text}')
        self.ids.name.text=''
    def animation_login(self):
        self.animation=Animation(duration=0, opacity=1)+Animation(duration=1, opacity=0)+Animation(duration=1, opacity=1)+Animation(duration=2,opacity=0)
        self.manager.get_screen('main').ids.welcome.text=f'WELCOME\n{self.ids.name.text}'
        self.animation.start(self.manager.get_screen('main').ids.welcome)
        self.animation=Animation(duration=8,opacity=0.8)
        self.animation.start(self.manager.get_screen('main').ids.wallpaper_main)

class setting(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def beta_volume(self, *args):
        self.ids.vol.text=f'volume {str(int(args[1]))}'
    def back(self):
        self.manager.current='main'
        self.manager.transition= SwapTransition()
    def switch(self):
        self.manager.current='change_wallpaper'
        self.manager.transition= FadeTransition()
class change_wallpaper(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def preview(self, file):
        try: 
            self.ids.preview.source=file[0]
        except:
            pass
    def change(self,file):
        main=self.manager.get_screen('main')
        try:
            main.ids.wallpaper_main.source=file[0]
        except:
            pass
    def back(self):
        self.manager.current='setting'
        self.manager.transition= SwapTransition()
class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def sett(self):
        self.manager.current='setting'
        self.manager.transition= FallOutTransition()
    def logout(self):
        self.manager.current='login'
        with open('../tryEverything.txt','w') as file:
            file.write('')
        self.manager.transition= WipeTransition()
    def spell(self):
        s=Spelling()
        word=self.ids.input.text
        self.ids.input.text=''
        s.select_language('en_US')
        try:
            option= s.suggest(word)
            x=''
            for i in range(5):
                x=f'{x} {option[i]}'
            self.ids.word.text=x
        except:
            self.ids.word.text='text was empty'
        
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation= Animation(duration=0, opacity=1)+Animation(duration=1, opacity=0)+Animation(duration=1, opacity=1)+Animation(duration=2,opacity=0)
        return Builder.load_file('tryEverything.kv')
    def build(self):
        self.sm = ScreenManager(transition= WipeTransition())
        self.sm.add_widget(login(name='login'))
        self.sm.add_widget(main(name='main'))
        self.sm.add_widget(setting(name='setting'))
        self.sm.add_widget(change_wallpaper(name='change_wallpaper'))
        with open('../tryEverything.txt','r') as file:
            if file.read()=='':
                self.sm.current='login'
            else:
                self.sm.current='main'
                self.sm.get_screen('main').ids.welcome.text=f'WELCOME \nBACK!!'
                self.animation.start(self.sm.get_screen('main').ids.welcome)
                self.animation=Animation(duration=8,opacity=0.8)
                self.animation.start(self.sm.get_screen('main').ids.wallpaper_main)
            return self.sm     
if __name__=='__main__':
    app().run()
    

