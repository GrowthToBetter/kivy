import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.menu import MDDropdownMenu
from kivy.resources import resource_add_path
import sys
import os
class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='LightBlue'
        self.theme_cls.accent_palette='Indigo'
        self.screen_manager=ScreenManager()
        self.screen_manager.add_widget(Builder.load_file(self.resource_path('login_surface.kv')))
        self.screen_manager.add_widget(Builder.load_file(self.resource_path('login_signup.kv')))
        self.screen_manager.add_widget(Builder.load_file(self.resource_path('login_main.kv')))
        text=['back to home', 'Log Out']
        menu=[{
            'text':text[i],
            'viewclass': 'OneLineListItem',
            'on_press':lambda x=i:self.back(x),
        } for i in range(2)]
        self.menu= MDDropdownMenu(
            caller=self.screen_manager.get_screen('main').ids.menu,
            items=menu,
            width_mult=4,
            size_hint=(None,None),
        )
        return self.screen_manager
    def back(self,x):
        if x==0:
            self.screen_manager.transition.direction='right'
            self.screen_manager.current='surface'
            self.menu.dismiss()
        else:
            self.screen_manager.transition.direction='right'
            self.screen_manager.current='signup'
            self.menu.dismiss()
    def resource_path(self , relative_path):
        try:
            base_path=sys._MEIPASS
        except Exception:
            base_path=os.path.abspath('kivy_project/SearchItem/')
        return os.path.join(base_path, relative_path)
    def signup(self):
        if self.screen_manager.get_screen('signup').ids.user.text !='' and self.screen_manager.get_screen('signup').ids.password.text !='':
            self.screen_manager.transition.direction='left'
            self.screen_manager.current='main'
            self.screen_manager.get_screen('signup').ids.user.text=''
            self.screen_manager.get_screen('signup').ids.password.text=''
        else:
            self.screen_manager.get_screen('signup').ids.alert.opacity=1
            animation= Animation(duration=1, opacity=0)
            animation.start(self.screen_manager.get_screen('signup').ids.alert)
if __name__=='__main__':
    if hasattr(sys, "_MEIPASS"):
        resource_add_path((os.path.join(sys._MEIPASS)))
    main().run()