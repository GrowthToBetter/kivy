import kivy
kivy.require('2.2.1')
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App
from kivy.animation import Animation

class main(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # current=self.ids.progress.value
        # if current ==0:
        #     for i in range(100):
        #         current=self.ids.progress.value
        #         current+=1
        #         self.ids.progress.value=current
        #         self.ids.progress_label.text=f'{current} %'
        # if self.ids.progress.value==100:
        #     self.ids.progress.value=0
        #     self.ids.progress_label.text=f'{current} %'
        anim= Animation(duration=20, value=100)+Animation(duration=0.000001, value=0 )
        anim.repeat= True
        anim.start(self.ids.progress)
        self.ids.say.text=f'{int(self.ids.progress.value)} %'
    def progress(self):
        # if self.ids.progress.value ==0:
        #     current=self.ids.progress.value
        #     current+=1
        #     self.ids.progress.value=current
        #     self.ids.progress_label.text=f'{current} %'
        # if self.ids.progress.value==100:
        #     self.ids.progress.value=0
        #     self.ids.progress_label.text=f'{current} %'
        self.ids.say.text=f'{int(self.ids.progress.value)} %'
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('progres.kv')
    def build(self):
        return main()

if __name__=='__main__':
    app().run()


