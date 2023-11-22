import kivy
from kivy.app import App
from kivy import *
kivy.require('2.1.0')
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#test
class myapp(App):
    def build(self):
        self.blyt= BoxLayout(orientation='vertical')
        btn1 = Button(text='dont click this!!',size_hint=(0.7,0.2),on_press=self.pressed1)
        btn2= Label(text= "None",size_hint=(0.9,0.5),)
        self.blyt.get_top()
        self.blyt.add_widget(btn1)
        self.blyt.add_widget(btn2)
        return self.blyt
    def pressed1(self,instance):
        btn3=Label(text= 'youre click this',size_hint=(0.7,0.2))
        self.blyt.add_widget(btn3)
        return self.blyt
if __name__=='__main__':
    myapp().run()