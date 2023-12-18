import kivy
kivy.require('2.2.1')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.graphics import Canvas, Rectangle, RoundedRectangle
from kivy.uix.button import  Button 
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('roundedbutton.kv')
class main(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def press(self):
        show=Label(
            text='hellow',
            size_hint=(0.1,0.2),
            pos_hint={'center_x':0.5,'y':0}

        )
        self.ids.button1.opacity=0
        return self.add_widget(show)


class app(App):
    def build(self):
        return main()
if __name__=='__main__':
    try:
        app().run()
    except:
        print('eror')