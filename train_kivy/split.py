import kivy
from kivy.uix.splitter import Splitter
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder 
from kivy.app import App
import copy
class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self, target ):
        sp=Splitter(sizable_from='left')
        box=BoxLayout(orientation='horizontal', size=(self.width,self.height))
        image= Image(opacity=0.5,source='')
        try:
            image.source=f'{target[0]}'
        except:
            pass
        box.add_widget(image)
        sp.add_widget(box)
        self.ids.wrap.add_widget(sp)

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('split.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm

if __name__=='__main__':
    app().run()