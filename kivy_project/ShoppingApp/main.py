from kivymd.app import MDApp, ThemeManager
from Fiture.manage import Manage, Content
import os, sys
from kivy.resources import resource_add_path
from kivymd.uix.expansionpanel import (
    MDExpansionPanel,
    MDExpansionPanelThreeLine,
)

class Load(Manage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette='LightBlue'
        self.Manage=Manage()
        self.Content=Content()
    def build(self):
        return Load().sm
    def on_start(self):
        for i in range(10):
            Load().sm.get_screen('list').ids.Items_shop.add_widget(
                MDExpansionPanel(
                    icon='./picture/Item1.jpeg',
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )
if __name__=="__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path((os.path.join(sys._MEIPASS)))

    MyApp().run()