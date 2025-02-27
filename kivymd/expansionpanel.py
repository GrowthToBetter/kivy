from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import(
      MDExpansionPanel,
      MDExpansionPanelThreeLine
)



class Content(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Test(MDApp):
    def build(self):
        return Builder.load_file('expansionpanel.kv')
    def on_start(self):
        for i in range(10):
            self.root.ids.box.add_widget(
                MDExpansionPanel(
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )
Test().run()

# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.toast import toast
# from kivymd.uix.bottomsheet import MDListBottomSheet

# KV = """
# MDScreen:

#     MDToolbar:
#         title: 'Example BottomSheet'
#         pos_hint: {'top': 1}
#         elevation: 10

#     MDRaisedButton:
#         text: 'Open list bottom sheet'
#         on_release: app.show_example_list_bottom_sheet()
#         pos_hint: {"center_x": .5, "center_y": .5}
# """


# class Example(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def callback_for_menu_items(self, list_item_text):
#         toast(list_item_text)

#     def show_example_list_bottom_sheet(self):
#         bottom_sheet_menu = MDListBottomSheet()
#         for i in range(1, 11):
#             bottom_sheet_menu.add_item(
#                 f"Standart Item {i}",
#                 lambda x, y=i: self.callback_for_menu_items(
#                     f"Standart Item {y}"
#                 ),
#             )
#         bottom_sheet_menu.open()


# Example().run()
