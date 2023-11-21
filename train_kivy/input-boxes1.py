import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
Builder.load_file('input-button1.kv')


class floatlayoutm(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def press(self):
        self.add_widget(Label(text=f'your name is {self.ids.name.text}'))

class app(App):
    def build(self):
        return floatlayoutm()
        
if __name__=='__main__':
    app().run()