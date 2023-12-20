import kivy
kivy.require('2.2.1')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

class main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def select(self,file):
        try:
            self.ids.pict.source=file[0]
        except:
            return False

class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('fileChooser.kv')
    def build(self):
        return main()
    
if __name__=='__main__':
    app().run()

