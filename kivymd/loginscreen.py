import kivy
kivy.require('2.2.1')
from kivy.lang import Builder
import kivymd
from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def press(self):
        if self.ids.user.text !='':
            self.ids.say.text=f'shut your mouth {self.ids.user.text}'
        else:
            self.ids.say.text='Please LOGIN'
    def clear(self):
        self.ids.user.text=''
        self.ids.pw.text=''
class mdapp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_pallete='LightGreen'
        self.theme_cls.accent_pallete='Teal'
        return Builder.load_file('loginscreen.kv')
    def build(self):
        return main()

mdapp().run()