import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
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
                        MDRaisedButton(
                            text="CANCEL"
                        ),
                        MDRaisedButton(
                            text="DISCARD"
                        ),
                    ],
            )
        self.dialog.open()
if __name__=='__main__':
    main().run()
    