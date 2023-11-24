import kivy
kivy.require("2.1.0")
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty

Builder.load_file('design-optimize.kv')
class main(FloatLayout):
    name= ObjectProperty(None)
    hobby= ObjectProperty(None)
    profesi= ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):
        self.content= self.ids.wrap
        self.name= self.content.name.text
        self.hobby= self.content.hobby.text
        self.profesi= self.content.profesi.text

        self.add_widget(Label(
            text=f"""nice to meet you, {self.name}
oh your work is {self.profesi}, and have {self.hobby} 
as your hobby right?..

""",
        size_hint=(0.4,0.5),
        pos_hint= {'x':0.3, 'y': 0}
        ))
        self.content.name.text= ''
        self.content.hobby.text= ''
        self.content.profesi.text= ''
class app(App):
    def build(self):
        return main()
    
if __name__=='__main__':
    app().run()