import kivy
from kivy.uix.splitter import Splitter
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.tab=TabbedPanel(do_default_tab=False)
        self.sp=Splitter(sizable_from='left')
        self.sp.add_widget(self.tab)
        self.count=0
        self.pic=[]
    def press(self, target ):
        self.pic.append(f'{target}')
        # box=BoxLayout(orientation='horizontal', size=(self.width,self.height))
        image= Image(opacity=0.5,source='')
        try:
            image.source=f'{target[0]}'
        except:
            pass
        # box.add_widget(image)
        # sp.add_widget(box)
        for i in range(len(self.pic)):
            item=TabbedPanelItem(text=f'tab {i}')
            item.add_widget(image)
        self.tab.add_widget(item)
        if self.count==0:
            self.ids.wrap.add_widget(self.sp)
            self.count=1
class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        return Builder.load_file('split.kv')
    def build(self):
        sm=ScreenManager()
        sm.add_widget(main(name='main'))
        return sm

if __name__=='__main__':
    app().run()