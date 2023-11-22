import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang.builder import BuilderBase

Builder= BuilderBase()

class load_name (GridLayout):
    def __init__(self,**kwargs):
        super(load_name,self).__init__(**kwargs)
        self.cols = 2
        self.rows =3
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class app(App):
    def build(self):
        ks=Label(text='selamat ')
        ks.pos=(315,400)
        kl=Label(text='datang!!! ')
        kl.pos =( 375,400)
        widget=Widget()
        widget.add_widget(ks) 
        widget.add_widget(kl) 
        return load_name()
        return widget
if __name__== "__main__":
    app().run()