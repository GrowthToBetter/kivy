from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import webbrowser
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.vkeyboard import VKeyboard



class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.borderless= True
        self.sm=ScreenManager()
        self.sm.add_widget(Builder.load_file('keyboard.kv'))
        ls_itm=['close', 'other']
        item=[{
            'text':f'{ls_itm[i]}',
            'viewclass':'OneLineListItem',
            'on_press':lambda x=i:self.press(ls_itm[x])
        }for i in range(len(ls_itm))]
        self.menu=MDDropdownMenu(
            caller=self.sm.get_screen('main').ids.menu,
            items=item,
            width_mult=4
        )
    def build(self):
        Keyboard=VKeyboard(on_key_up=self.key_up)
        self.sm.get_screen('main').ids.vkey.add_widget(Keyboard)
        return self.sm
    def change(self, condition):
        if condition=='Light':
            self.theme_cls.theme_style ='Dark'
        else:
            self.theme_cls.theme_style ='Light'
    def press(self, category):
        if category=='close':
            self.stop()
        else:
            webbrowser.open('https://kivy.org')
    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode,tuple):
            keycode=keycode[1]
        previous=self.sm.get_screen('main').ids.word.text
        if keycode=='spacebar':
            keycode=' '
        if keycode=='backspace':
            previous=previous[:-1]
            keycode=''
        self.sm.get_screen('main').ids.word.text= f'{previous}{keycode}'
        
if __name__=="__main__":
    MyApp().run()