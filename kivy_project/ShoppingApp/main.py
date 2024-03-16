from kivymd.app import MDApp, ThemeManager
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from Fiture import list_item
class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm=ScreenManager()
        self.theme_cls.primary_palette='LightBlue'
 

    def build(self):
        return self.sm

if __name__=="__main__":
    MyApp().run()