from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.swiper import *
from kivymd.utils.fitimage import FitImage
class app(MDApp):
    def build(self):
        self.img=[]
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='DeepOrange'
        self.theme_cls.accent_palette='Yellow'
        self.i=0
        return Builder.load_file('swipImg.kv')
    def select(self, img):
        self.img.append(img[0])
    def press(self):
        if self.i+1 <= len(self.img):
            swip= MDSwiperItem()
            item=FitImage(
                    radius=[20,],
                    source=f'{self.img[self.i]}',
                    )
            swip.add_widget(item)     
            self.root.ids.swip.add_widget(swip)
            self.i+=1
app().run()