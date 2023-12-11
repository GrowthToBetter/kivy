import kivy
kivy.require('2.1.0')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ColorProperty,ObjectProperty
from kivy.input.motionevent import MotionEvent
from kivy.factory import Factory
import asynckivy as ak
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy_garden.draggable import KXDroppableBehavior, KXDraggableBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

KV_CODE = '''
<loading>:
    name:'load'
    FloatLayout:
        size: root.width,root.height
        id:container
        Image:
            id: bg
            source:'background.jpg'
            keep_ratio : False
            size_hint: 1, 1
            allow_stretch: True
        Image:
            id:logo
            source:'smpn1pogalan.png'
            keep_ratio: 0.3
            pos_hint:{'center_x':0.5,'center_y':0.5}
        Label:
            text: 'PERIODIC TABEL FOR STUDENT'
            font_size: 60
            size_hint:5,5
            pos_hint: {'center_x':0.51, 'center_y':0.09}
            color: 0,100/255,40/255,5

        Label:
            id:jd
            text: 'PERIODIC TABEL FOR STUDENT'
            font_size: 60
            size_hint:5,5
            pos_hint: {'center_x':0.5, 'center_y':0.1}
            color: 0,230/255,100/255,5
    FloatLayout:
        TextInput:
            id: akun
            pos_hint: {'center_x':0.5,'center_y':0.3}
            multiline:False
            size_hint:0.35,0.045
        Label:
            text:'akun'
            bold: True
            pos_hint: {'center_x': 0.3, 'center_y': 0.3}
            size_hint: 1,1
            color:0,0,0,1
        TextInput:
            id: pw
            pos_hint: {'center_x':0.5,'center_y':0.25}
            multiline:False
            size_hint:0.35,0.045
        Label:
            text:'password'
            bold: True
            pos_hint: {'center_x': 0.2888888, 'center_y': 0.25}
            size_hint: 1,1
            color:0,0,0,1
        Button:
            text:'submit'
            id: submit
            bold: True
            size_hint:0.35,0.045
            pos_hint: {'center_x':0.5,'center_y':0.2}
            color: 0,0,1,1
            background_color: 0,0,200/255,1
            on_release: 
                root.check_credentials(akun.text, pw.text)
                
                

<DroppableArea>:
    drag_classes: ['exam', ]
    canvas.before:
        Color:
            rgba: self.line_color
        Line:
            width: 2
            rectangle: [*self.pos, *self.size, ]
        
<DraggableLabel>:
    drag_cls: 'exam'
    drag_timeout: 0
    font_size: 30
    opacity: .4 if root.is_being_dragged else 1.
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Line:
            dash_length: 4
            dash_offset: 4
            rectangle: [*self.pos, *self.size, ]
    FloatLayout:
        id:noun


<core>:
    name:'main sys'
    FloatLayout:
        Image:
            id:logo
            source:'smpn1pogalan.png'
            keep_ratio: 0.3
            pos_hint:{'center_x':0.5,'center_y':0.5}
            opacity: 0.5
        Label:
            color: "#FF0000"
            text: 'logam'
            font_size:30
            pos_hint:{'center_x':0.25,'center_y':0.8}
        Label:
            color: "#00FF00"
            text: 'nonlogam'
            font_size:30
            pos_hint:{'center_x':0.25,'center_y':0.5}
        Label:
            color: "#0000FF"
            text: 'metaloid'
            font_size:30
            pos_hint:{'center_x':0.25,'center_y':0.2}
    BoxLayout:
        id:container
        orientation: 'horizontal'
        spacing: 50
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20
            DroppableArea:
                line_color: "#FF0000"
                color_cls: 'logam'
            
            DroppableArea:
                line_color: "#00FF00"
                color_cls: 'nonlogam'
            
            DroppableArea:
                line_color: "#0000FF"
                color_cls: 'metaloid'
            
        GridLayout:
            id:where_the_items_initially_live
            cols: 3
            padding: 20
            spacing: 20
            ScrollView:
                id:scroll
                size_hint_x: 5
                width: root.width * 0.6
                do_scroll_Y: True
                scroll_y: 1 
'''


root=Builder.load_string(KV_CODE)
class DraggableLabel(KXDraggableBehavior, Factory.Label):
    color_cls = StringProperty()
    label_widget = ObjectProperty()
    label= ObjectProperty()
    correct_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DraggableLabel,self).__init__(**kwargs)
        self.amount=0
    def on_drag_fail(self, touch):
        ctx = self.drag_context
        if ctx.droppable is not None:
            if hasattr(self,'label'):
                self.parent.remove_widget(self.label)
            self.label = Label(
                text=f"Salah! {self.text} Tidak Bertipe {ctx.droppable.color_cls}",
                bold=True,
                color=(1,1,0,1),
                size_hint=(None, None),
                size=(400, 30),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
            )
            self.parent.add_widget(self.label)  # Tambahkan label baru
            self.animate() 
        return super().on_drag_fail(touch)
    def animate(self):
        animation=Animation(opacity=0,duration=1)+Animation(opacity=1,duration=1)
        animation.repeat= True
        animation.start(self.label)
    async def on_drag_success(self, touch):
        self.center = self.to_window(*self.drag_context.droppable.center)
        await ak.animate(self, opacity=0, d=0.5)
        self.correct_label=Label(
                text=f"Correct",
                size_hint=(None, None),
                bold=True,
                size=(400, 30),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
            )
        if self.parent and self.label:
            self.parent.remove_widget(self.label)
        if self.parent and self.correct_label:
            self.parent.add_widget(self.correct_label)
            await ak.sleep(0.5)
            if self.parent and self.correct_label:
                self.parent.remove_widget(self.correct_label)
            if self.parent:
                self.parent.remove_widget(self)
class DroppableArea(KXDroppableBehavior, Factory.FloatLayout):
    line_color = ColorProperty()
    color_cls = StringProperty()
    label_widget = ObjectProperty(None)
    existing_label=None
    def accepts_drag(self, touch, draggable):
        if draggable.color_cls == self.color_cls:
            DraggableLabel.label_widget=None
            if self.existing_label:
                self.remove_widget(self.existing_label)  
                self.existing_label = None 
                self.existing_label = draggable.label 
                if self.existing_label: 
                    self.existing_label = None 
                    self.parent.remove_widget(self) 
                         
            return True

class core(Screen):

    def __init__(self, **kw):
        super(core,self).__init__(**kw)
        self.grid_layout=self.ids.where_the_items_initially_live.add_widget
        self.scrollview=self.ids.scroll.add_widget
        items=[]
        for color_cls, names in {
            'logam': ('Fe', 'Li', 'Be', 'Ca', 'Na', 'Mg', 'K', 'Ca', 'Rb', 'Sr', 'Cs', 'Ba', 'Sc', 'Y', 'Lu', 'Ti', 'Zz', 'Hf',
                      'V', 'Nb', "Ta", 'Cr', 'Mo', 'W', 'Mn', 'Tc', 'Re', 'Ru', 'Os', 'Co', 'Rh', 'Ir', 'Ni', 'Pd', 'Pt', 'Cu',
                      'Ag', 'Au', 'Zn', 'Cd', 'Al', 'Ti', 'Ga', 'In', 'Sn', 'Pb', 'Bi', 'Po'
                      ),
            'nonlogam': ('He', 'Ne', 'O', 'H', 'Ar', 'Kr', 'Xe', 'Rn', 'F', 'Cl', 'Br', 'I', 'At', 'S', 'Se', 'N', 'P', 'C'),
            'metaloid': ('B', 'Ge', 'Si', 'As', 'Te'),
        }.items():
            for idx, name in enumerate(names):
                if idx<=10:
                    items.append(DraggableLabel(text=name, color_cls=color_cls))    

        from random import shuffle
        shuffle(items)
        for item in items:
            self.grid_layout(item)
class Loading(Screen):
    akun=['SMPN1POGALAN',]
    password=['SNEPOGA',]
    error_label = None
    def __init__(self, **kw):
        super(Loading, self).__init__(**kw)
        self.is_input_correct = False
    def animate(self,id):
        animation = Animation(
            size_hint=(0.12, 0.109),
            duration=0.5
        ) + Animation(
            size_hint=(0.1, 0.1),
            duration=0.5
        )
        animation.repeat = True
        return animation.start(id)
    def check_credentials(self, akun_text, pw_text):
        if akun_text in self.akun and pw_text in self.password :
            self.is_input_correct = True
            self.manager.current ='main sys'
            if self.is_input_correct:
                self.manager.current = 'main sys'
        else:
            self.is_input_correct = False
            self.ids.akun.text = ''
            self.ids.pw.text = ''
            self.change()
            self.add_error_label("Incorrect credentials. Please try again.")
            return False
    def add_error_label(self, text):
        if self.error_label:
            self.ids.container.remove_widget(self.error_label)
        self.error_label = Label(
            text=text,
            size_hint=(None, None),
            size=(400, 30),
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            color=(1, 0, 0, 1)
        )
        self.ids.container.add_widget(self.error_label)
    def change(self):
        if not self.is_input_correct:
            self.ids.akun.text = ''
            self.ids.pw.text = ''
            self.is_input_correct=False
        else:
            self.manager.switch_to(core(name='main sys'))
class ScreenManagerApp(App):
    def build(self):
        self.sm = ScreenManager()
        loading_screen = Loading(name='load')
        self.sm.add_widget(loading_screen)
        self.sm.add_widget(Loading(name='load'))
        self.sm.add_widget(core(name='main sys'))
        loading_screen.manager = self.sm
        self.sm.current = 'load'
        return self.sm
    def on_start(self):
        self.title='periodic for student'

if __name__ == '__main__':
    app = ScreenManagerApp()
    app.run()

