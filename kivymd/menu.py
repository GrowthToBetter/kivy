import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFloatingActionButtonSpeedDial


class main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        self.theme_cls.primary_palette='Cyan'
        self.sm =ScreenManager()
        self.sm.add_widget(Builder.load_file('menu.kv'))
        items=['bara', 'jean','testing']
        item=[{
            'text':f'{items[i]}',
            'viewclass':'OneLineListItem',
            'on_press':lambda x=i:self.change(items[x])
        }for i in range(len(items))
        ]
        self.menu= MDDropdownMenu(
            caller=self.sm.get_screen('main').ids.menu,
            items=item,
            width_mult=4
        )
        return  self.sm
    def change(self,item):
        self.sm.get_screen('main').ids.say.text=f'{item}'
        self.menu.dismiss()
main().run()
    