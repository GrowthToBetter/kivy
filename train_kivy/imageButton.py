import kivy
kivy.require('2.2.1')
from kivy.uix.widget import Widget
from kivy.lang import  Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

class main(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def press(self):
        self.ids.log.size_hint=0.15,0.45
        self.ids.say.text='press'
        self.ids.but.source='D:/study-coding/picture/New-Folder/9.jpeg'
    def release(self):
        self.ids.log.size_hint=0.2,0.5
        self.ids.say.text='dont press'
        self.ids.but.source='D:/study-coding/picture/New-Folder/2.jpeg'
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('imageButton.kv')
    
    def build(self):
        return main()
    
if __name__=='__main__':
    app().run()