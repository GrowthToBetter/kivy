from kivymd.app import MDApp, ThemeManager
from Fiture.manage import Manage
import os, sys
from kivy.resources import resource_add_path


class Load(Manage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette='LightBlue'

    def build(self):
        return Load().sm

if __name__=="__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path((os.path.join(sys._MEIPASS)))

    MyApp().run()