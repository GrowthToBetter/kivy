import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

class app(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Red'
        self.sm=ScreenManager()
        self.sm.add_widget(Builder.load_file('bottombar.kv'))
        return self.sm
    def press(self, action):
        self.sm.get_screen('main').ids.say.text=f'you press {action}'
if __name__=='__main__':
    app().run()