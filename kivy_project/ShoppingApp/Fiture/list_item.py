import kivy
kivy.require('2.2.1')
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager


class Shop_mecanic(MDScreen):
    def __init__(self) -> None:
        self.screen= ScreenManager()
        return Builder.load_file('Fiture/list_item.kv')

