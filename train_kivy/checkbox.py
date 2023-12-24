import kivy
kivy.require('2.2.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.app import App

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self,instance, value):
        if value==True:
            if instance==1:
                self.ids.picture.source='d:/study-coding/picture/New-Folder/shower.jpeg'
            if instance==2:
                self.ids.picture.source='d:/study-coding/picture/New-Folder/cosE.jpg'
        else:        
           self.ids.picture.source='C:/Users/ASUS/Downloads/images (1).jpeg'
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('checkbox.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm
if __name__=='__main__':
    app().run()


        