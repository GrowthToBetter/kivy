import kivy
kivy.require('2.1.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
 
Builder.load_file('input-box2.kv')

class main(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def input(self):
        self.name= self.ids.txt.text
        self.add_widget(Label(
            text=f'your name is {self.name}',
            size_hint=(0.4,0.4),
            pos_hint={'x':0.4,'y':0}
                              ))
class app(App):
    def build(self):
        return main()
    
if __name__=='__main__':
    app().run()