import kivy 
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('train 5.kv')
class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid,self).__init__(**kwargs)
    def change_label(self):
        self.ids.label1.text='bad choice!!'   
    def back(self):
        self.ids.label1.text='have fun!!'
class app(App):
    def build(self):
        return Grid()

if __name__=='__main__':
    app().run()