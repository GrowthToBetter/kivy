import kivy
kivy.require('2.2.1')
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class app(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='DeepPurple'
        self.theme_cls.accent_palette='Blue'
        return Builder.load_file('kivymdfirst.kv')
    def build(self):

        return main()
app().run()