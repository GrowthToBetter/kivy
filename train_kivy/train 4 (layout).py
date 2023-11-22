##box layout ->  Layout ini digunakan untuk mengatur tata letak elemen GUI menjadi sebuah kotak atau persegi panjang. 
##BoxLayout dapat berorientasi horizontal atau vertikal.

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button


# class MyBoxLayout(BoxLayout):
#     def __init__(self, **kwargs):
#         super(MyBoxLayout, self).__init__(**kwargs)
#         self.orientation = 'vertical'

#         for i in range(6):
#             btn = Button(text=f'Button {i+1}')
#             self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyBoxLayout()


# if __name__ == '__main__':
#     MyApp().run()

##grid layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI dalam bentuk grid atau tabel.

# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button


# class MyGridLayout(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGridLayout, self).__init__(**kwargs)
#         self.cols = 2

#         for i in range(4):
#             btn = Button(text=f'Button {i+1}')
#             self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyGridLayout()


# if __name__ == '__main__':
#     MyApp().run()

##float layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI dengan posisi yang relatif terhadap ukuran dan posisi window.

# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.button import Button


# class MyFloatLayout(FloatLayout):
#     def __init__(self, **kwargs):
#         super(MyFloatLayout, self).__init__(**kwargs)
#         btn1 = Button(text='Button 1', size_hint=(.2, .2), pos_hint={'x': .1, 'y': .5})
#         btn2 = Button(text='Button 2', size_hint=(.2, .2), pos_hint={'x': .7, 'y': .5})
#         btn3 = Button(text='Button 3', size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .3})

#         self.add_widget(btn1)
#         self.add_widget(btn2)
#         self.add_widget(btn3)


# class MyApp(App):
#     def build(self):
#         return MyFloatLayout()


# if __name__ == '__main__':
#     MyApp().run()

##relative layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI dengan posisi yang relatif terhadap elemen lainnya 
##atau posisi relatif terhadap window., 
##Layout RelativeLayout digunakan untuk mengatur tata letak elemen GUI dengan mengatur posisi elemen relatif terhadap elemen lain di dalam tata letak.
##Layout ini berguna ketika elemen-elemen tersebut perlu ditempatkan secara relatif terhadap satu sama lain.

# from kivy.app import App
# from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.button import Button


# class MyRelativeLayout(RelativeLayout):
#     def __init__(self, **kwargs):
#         super(MyRelativeLayout, self).__init__(**kwargs)

#         # Tambahkan dua button dengan posisi relatif terhadap anchor
#         btn1 = Button(text='Button 1', size_hint=(.2, .2))
#         btn2 = Button(text='Button 2', size_hint=(.2, .2))

#         self.add_widget(btn1)
#         self.add_widget(btn2)

#         # Atur posisi Button 1
#         btn1.pos_hint = {'center_x': .5, 'center_y': .5}

#         # Atur posisi Button 2 secara relatif terhadap Button 1
#         btn2.pos_hint = {'center_x': btn1.pos_hint['center_x'] - .2, 'center_y': btn1.pos_hint['center_y'] - .2}


# class MyApp(App):
#     def build(self):
#         return MyRelativeLayout()


# if __name__ == '__main__':
#     MyApp().run()


##scatter layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI yang dapat dirotasi, diubah ukurannya dan dipindahkan (dalam 2D).
##Biasanya digunakan untuk menambahkan efek 2D pada elemen GUI seperti zoom, rotasi, dan translasi.

# from kivy.app import App
# from kivy.uix.scatterlayout import ScatterLayout
# from kivy.uix.button import Button


# class MyScatterLayout(ScatterLayout):
#     def __init__(self, **kwargs):
#         super(MyScatterLayout, self).__init__(**kwargs)

#         for i in range(3):
#             btn = Button(text=f'Button {i+1}')
#             self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyScatterLayout()


# if __name__ == '__main__':
#     MyApp().run()

##anchor layout ->  Layout ini digunakan untuk mengatur tata letak elemen GUI dengan mengikat elemen ke titik tertentu di dalam window
##seperti bagian atas, tengah, atau bawah.

# from kivy.app import App
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.button import Button


# class MyAnchorLayout(AnchorLayout):
#     def __init__(self, **kwargs):
#         super(MyAnchorLayout, self).__init__(**kwargs)
#         btn = Button(text='Button', size_hint=(.2, .2), pos_hint={'center_x': .5, 'center_y': .5})

#         self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyAnchorLayout()


# if __name__ == '__main__':
#     MyApp().run()

##page layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI dalam beberapa halaman atau tab yang dapat dipindahkan.

# from kivy.app import App
# from kivy.uix.pagelayout import PageLayout
# from kivy.uix.button import Button


# class MyPageLayout(PageLayout):
#     def __init__(self, **kwargs):
#         super(MyPageLayout, self).__init__(**kwargs)

#         for i in range(3):
#             btn = Button(text=f'Page {i+1}')
#             self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyPageLayout()


# if __name__ == '__main__':
#     MyApp().run()

##stack layout -> Layout ini digunakan untuk mengatur tata letak elemen GUI dalam urutan stack.

# from kivy.app import App
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.button import Button


# class MyStackLayout(StackLayout):
#     def __init__(self, **kwargs):
#         super(MyStackLayout, self).__init__(**kwargs)

#         for i in range(3):
#             btn = Button(text=f'Button {i+1}')
#             self.add_widget(btn)


# class MyApp(App):
#     def build(self):
#         return MyStackLayout()


# if __name__ == '__main__':
#     MyApp().run()
