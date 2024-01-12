from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker

class main(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette ='Yellow'
        return Builder.load_file('date.kv')
    def ok(self, obj, value, range):
        # self.root.ids.say.text=f'{str(value)}'
        self.root.ids.say.text=f'{str(range[0])} - {str(range[-1])}'
    def cancel(self,obj,value):
        self.root.ids.say.text='canceling'
    def click(self):
        self.date= MDDatePicker(mode='range')
        self.date.bind(on_save=self.ok, on_cancel=self.cancel)
        self.date.open()

main().run()