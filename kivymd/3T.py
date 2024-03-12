from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm= ScreenManager()
        self.sm.add_widget(Builder.load_file('3T.kv'))
        self.turn=0
        self.score_x=0
        self.score_o=0
    def build(self):
        return self.sm
    def combination(self):
        obj= self.sm.get_screen('main')
        if obj.ids.b1.text == obj.ids.b2.text and obj.ids.b1.text == obj.ids.b3.text and obj.ids.b1.text !='':
            self.end(obj.ids.b1.text)
        elif obj.ids.b4.text == obj.ids.b5.text and obj.ids.b4.text == obj.ids.b6.text and obj.ids.b4.text !='':
            self.end(obj.ids.b4.text)
        elif obj.ids.b7.text == obj.ids.b8.text and obj.ids.b7.text == obj.ids.b9.text and obj.ids.b7.text !='':
            self.end(obj.ids.b7.text)
        elif obj.ids.b1.text == obj.ids.b4.text and obj.ids.b1.text == obj.ids.b7.text and obj.ids.b1.text !='':
            self.end(obj.ids.b1.text)
        elif obj.ids.b2.text == obj.ids.b5.text and obj.ids.b2.text == obj.ids.b8.text and obj.ids.b2.text !='':
            self.end(obj.ids.b2.text)
        elif obj.ids.b3.text == obj.ids.b6.text and obj.ids.b3.text == obj.ids.b9.text and obj.ids.b3.text !='':
            self.end(obj.ids.b3.text)
        elif obj.ids.b3.text == obj.ids.b5.text and obj.ids.b3.text == obj.ids.b7.text and obj.ids.b3.text !='':
            self.end(obj.ids.b3.text)
        elif obj.ids.b1.text == obj.ids.b5.text and obj.ids.b1.text == obj.ids.b9.text and obj.ids.b1.text !='':
            self.end(obj.ids.b1.text)
    def press(self,id,text):
        if self.turn==0 and text=='':
            id.text='x'
            self.turn=1
            self.combination()
        elif self.turn ==1 and text=='':
            id.text='o'
            self.turn=0
            self.combination()
        self.sm.get_screen('main').ids.scorex.text=f'score x is {self.score_x}'
        self.sm.get_screen('main').ids.scoreo.text=f'score o is {self.score_o}'
    def end(self, text):
        obj= self.sm.get_screen('main')
        obj.ids.b1.disabled= True
        obj.ids.b2.disabled= True
        obj.ids.b3.disabled= True
        obj.ids.b4.disabled= True
        obj.ids.b5.disabled= True
        obj.ids.b6.disabled= True
        obj.ids.b7.disabled= True
        obj.ids.b8.disabled= True
        obj.ids.b9.disabled= True
        if text=='x':
            self.score_x +=1
        if text == 'o':
            self.score_o +=1
    def referesh(self):
        obj= self.sm.get_screen('main')
        self.turn=0
        obj.ids.b1.disabled= False
        obj.ids.b2.disabled= False
        obj.ids.b3.disabled= False
        obj.ids.b4.disabled= False
        obj.ids.b5.disabled= False
        obj.ids.b6.disabled= False
        obj.ids.b7.disabled= False
        obj.ids.b8.disabled= False
        obj.ids.b9.disabled= False

        obj.ids.b1.text= ''
        obj.ids.b2.text= ''
        obj.ids.b3.text= ''
        obj.ids.b4.text= ''
        obj.ids.b5.text= ''
        obj.ids.b6.text= ''
        obj.ids.b7.text= ''
        obj.ids.b8.text= ''
        obj.ids.b9.text= ''
if __name__=="__main__":
    MyApp().run()