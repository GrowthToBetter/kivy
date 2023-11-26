import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

Builder.load_file('try-box.kv')
akun=['bara']
pw=['123']
class main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press(self):

        self.name=self.ids.name.text
        self.password=self.ids.pw.text
        if self.name==akun[0] and self.password==pw[0]:
                self.ids.wrap.add_widget(
                    Label(
                        text='log in',
                        size_hint=(0.4,0.4),
                        pos_hint={'center_x':0.5,'center_y':0.3}

                    )
                )
        else:
            self.ids.wrap.add_widget(
                    Label(
                        text='password atau akun salah',
                        size_hint=(0.4,0.4),
                        pos_hint={'center_x':0.5,'center_y':0.3}

                    )
                )
        self.ids.name.text=''
        self.ids.pw.text=''
class app(App):
    def build(self):
        return main()

if __name__=='__main__':
    app().run()
