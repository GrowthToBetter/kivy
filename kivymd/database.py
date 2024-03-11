from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
import sqlite3
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm= ScreenManager()
        self.sm.add_widget(Builder.load_file('database.kv'))
        self.list_menu=['data','main','server']
        item=[{
            'text':f'{self.list_menu[i]}',
            'viewclass': 'OneLineListItem',
            'on_press': lambda x=i: self.open(x),
        }for i in range(len(self.list_menu))]
        self.descrip=MDDropdownMenu(
            caller=self.sm.get_screen('main').ids.menu,
            items=item,
            width_mult=4
        )
    def open(self,index):
        if index == 0:
            self.sm.get_screen('main').ids.menu.title='D A T A'
        elif index == 2:
            self.sm.get_screen('main').ids.menu.title='S E R V E R'
        else:
            self.sm.get_screen('main').ids.menu.title='M    E   N   U'
        
    def build(self):
        conn=sqlite3.connect('database.db')

        c=conn.cursor()
        c.execute("""CREATE TABLE if not exists jadwal(
                name text
                day text
        )
""")
        conn.commit()
        conn.close()
        return self.sm
    def submit(self):
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        c.execute("INSERT INTO jadwal VALUES (:name)",
            {'name':self.sm.get_screen('main').ids.input.text}
                  
)
        c.execute("INSERT INTO jadwal VALUES (:day)",
            {'day':self.sm.get_screen('main').ids.input2.text}
                  
)
        self.sm.get_screen('main').ids.word.text='succesfully add'
        self.sm.get_screen('main').ids.input.text=''
        self.sm.get_screen('main').ids.input2.text=''
        conn.commit()
        conn.close()
    def show(self):
        conn=sqlite3.connect('database.db')
        c=conn.cursor()
        c.execute(" SELECT * FROM jadwal "
)
        records=c.fetchall()
        for i in range(len(records)):
            if i%2==1: 
                self.label=MDLabel(
                    text=f'{records[i]}',
                    halign='center'
                )
                self.sm.get_screen('main').ids.tabel.add_widget(self.label)
            if i%2==0:
                self.label=MDLabel(
                    text=f'{records[i]}',
                    halign='center'
                )
                self.sm.get_screen('main').ids.tabel.add_widget(self.label)
        conn.commit()
        conn.close()
if __name__=="__main__":
    MyApp().run()