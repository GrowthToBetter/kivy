import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class app(MDApp):
    def build(self):
        self.sm=ScreenManager()
        self.sm.add_widget(Builder.load_file('navbar.kv'))
        return self.sm
    
if __name__=='__main__':
    app().run()