import kivy
kivy.require('2.2.1')
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
import os, sys
from kivy.core.window import Window

class Manage(MDScreen):
    def __init__(self, **kwargs):
        self.sm= ScreenManager()
        self.sm.add_widget(Builder.load_file(self.Resource_path('Fiture/surface.kv')))
    def Resource_path(self,Relative_path):
        try:
            Base_path=sys._MEIPASS
        except Exception:
            Base_path=os.path.abspath('kivy_project/ShoppingApp/')
        return os.path.join(Base_path, Relative_path)
    def press(self, definition):
        print(f'{definition}')