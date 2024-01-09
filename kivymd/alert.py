import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import *
class main(MDApp):
    dialog=None
    def build(self):
        self.theme_cls.primary_palette='Red'
        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file('alert.kv'))
        return self.sm
    def call(self):
        if not self.dialog:
            self.dialog=MDDialog(
                text='tes',
                buttons=[
                        MDRoundFlatButton(
                            text="CANCEL", 
                            text_color= self.theme_cls.primary_color, 
                            on_press=self.close
                        ),
                        MDRaisedButton(
                            text="DISCARD", 
                            text_color= self.theme_cls.primary_color, 
                            md_bg_color= (1,1,1,1), 
                            on_press=self.press
                        ),
                    ],
            )
        self.dialog.open()
    def close(self, type):
        self.dialog.dismiss()
        self.sm.get_screen('main').ids.say.text='welcome'
    def press(self, type):
        self.dialog.dismiss()
        self.sm.get_screen('main').ids.say.text='heloo'

if __name__=='__main__':
    main().run()
    