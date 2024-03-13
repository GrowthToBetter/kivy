from kivymd.app import MDApp
from kivy.lang import Builder 
import webbrowser
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
import sqlite3
from kivymd.uix.label import MDLabel
class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm=ScreenManager()
        self.sm.add_widget(Builder.load_file('database2.kv'))
        list_menu=['show','learn more']
        items=[{
            'text':f'{list_menu[i]}',
            'viewclass':'OneLineListItem',
            'on_press':lambda x=i:self.classification(x)
        } for i in range(len(list_menu))]
        self.menu= MDDropdownMenu(
            items=items,
            caller=self.sm.get_screen('main').ids.menu,
            width_mult=4
        )
    def build(self):
        return self.sm
    def classification(self, num):
        if num == 0:
            self.show()
            self.menu.dismiss()
        if num == 1:
            webbrowser.open('https://github.com/GrowthToBetter')
    def show(self):
        conn= sqlite3.connect('database.db')
        c= conn.cursor()
        c.execute('SELECT * FROM jadwal')
        data= c.fetchall()
        for i in range(len(data)):
            self.sm.get_screen('main').ids.word.add_widget(
                MDLabel(
                    halign='center',
                    text=f'{data[i]}'
                )
            )
        conn.commit()
        conn.close
if __name__=="__main__":
    MyApp().run()