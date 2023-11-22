import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
Builder.load_file('train 12.kv')
st=False
lv=0
class main(FloatLayout):
    def start(self):
        start1= Button(text="start", pos_hint={'x':0.2,'y':0.3})
        start1.on_press=True
        return True
    def loop(self):
        if self.start():
            bttn=[1,2,3,4]
            for i in bttn:
                bnew=self.ids.ttt
                

class app(App):
    def build(self):
        return main
    
if __name__=='__main__':
    app().run()