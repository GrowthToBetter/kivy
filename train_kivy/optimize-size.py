import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.textinput import TextInput


Builder.load_file('optimize-size.kv')
class main(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def submit(self):
        self.name= self.ids.input.text
        self.add_widget(Label(
            text=f"your name is {self.name}",
            size_hint=(None,None),
            width=150,
            height=25,
            pos_hint={'x':0.4,'y':0.55}
            ))
        
class app(App):
    def build(self):
        return main()
    
if __name__ == '__main__':
    app().run()