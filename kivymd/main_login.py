import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.animation import Animation
Window.size=(400,600)

class main(MDApp):
    def build(self):
        self.screen_manager=ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('login_surface.kv'))
        self.screen_manager.add_widget(Builder.load_file('login_signup.kv'))
        self.screen_manager.add_widget(Builder.load_file('login_main.kv'))
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='LightBlue'
        return self.screen_manager
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
    main().run()