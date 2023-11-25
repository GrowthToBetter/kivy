import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import  Builder
from kivy.app import App
from kivy.properties import ObjectProperty


Builder.load_file('design-color.kv')

class main(FloatLayout):
    name= ObjectProperty(None)
    hobby= ObjectProperty(None)
    profesi= ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def press(self):
        self.name=self.ids.wrap.name
        self.hobby=self.ids.wrap.hobby
        self.profesi=self.ids.wrap.profesi
        self.add_widget(Label(
            text=f"""{self.name},
            have {self.hobby} as the hobby
            and have {self.profesi} as the profesi""",
            size_hint=(0.4,0.5),
            pos_hint={'x':0.3,'y':0}
            
            ))
        self.ids.wrap.name=''
        self.ids.wrap.hobby=''
        self.ids.wrap.profesi=''
class app(App):
    def build(self):
        return main()
    

if __name__=='__main__':
    app().run()