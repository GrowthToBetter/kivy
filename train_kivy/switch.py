import kivy
kivy.require('2.2.1')
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self, value):
        if value:
            self.ids.say.text='wallpaper on'
            self.ids.img.opacity=1
        else:
            self.ids.say.text='wallpaper off'
            self.ids.img.opacity=0

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('switch.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm
    
if __name__=='__main__':
    app().run()