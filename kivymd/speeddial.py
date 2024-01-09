from kivy.lang import Builder
from kivymd.app import MDApp


class app(MDApp):
    data={
        'Python':'language-python',
        'Ruby':'language-ruby',
        'JS':'language-javascript'
    }

    def build(self):
        self.theme_cls.primary_palette='Amber'
        return Builder.load_file('speeddial.kv')
    def call(self, num):
        self.root.ids.say.text = f'You pressed {num.icon}'

app().run()