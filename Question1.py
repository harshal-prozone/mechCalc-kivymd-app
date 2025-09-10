from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.core.text import LabelBase
from PIL import Image
from kivymd.uix.dialog import MDDialog
from math import *
from kivymd.uix.button import *
image_path = 'C:\\Users\\sreej\\OneDrive\\Documents\\Student\\Sem - 1\\Mechanics\\Question1.png'
image = Image.open(image_path)
Window.size = image.size

KV = '''
FloatLayout:
    Image:
        id:background_image
        source: 'Mechanics\\Question1.png'
        allow_stretch: True
        keep_ratio: False

    MDTextField:
        id: input_f
        mode: "fill"
        multiline: False
        fill_color_normal: "#ffffff"
        fill_color_focus: "#ffffff"
        line_color_focus: "#ca765b"
        text_color_normal: "#ca765b"
        text_color_focus: "#ca765b"
        font_name:"Kodchasan"
        size_hint_x: 0.15
        size_hint_y: 0.06
        pos_hint: {"center_x": 0.8, "center_y": 0.8}

    MDTextField:
        id: input_alpha
        mode: "fill"
        multiline: False
        fill_color_normal: "#ffffff"
        fill_color_focus: "#ffffff"
        line_color_focus: "#ca765b"
        text_color_normal: "#ca765b"
        text_color_focus: "#ca765b"
        font_name:"Kodchasan"
        size_hint_x: 0.15
        size_hint_y: 0.06
        pos_hint: {"center_x": 0.8, "center_y": 0.715}

    MDTextField:
        id: input_beta
        mode: "fill"
        multiline: False
        fill_color_normal: "#ffffff"
        fill_color_focus: "#ffffff"
        line_color_focus: "#ca765b"
        text_color_normal: "#ca765b"
        text_color_focus: "#ca765b"
        font_name:"Kodchasan"
        size_hint_x: 0.15
        size_hint_y: 0.06
        pos_hint: {"center_x": 0.8, "center_y": 0.63}

    MDFillRoundFlatButton:
        size_hint: 0.2, 0.07
        md_bg_color: 1, 1, 1, 0
        pos_hint: {"center_x": 0.665, "center_y": 0.5}
        on_press: app.on_continue()
'''

class ForceComponentsApp(MDApp):
    dialog = None
    added_labels = []
    
    def build(self):
        self.title = "Force Components Input"
        return Builder.load_string(KV)

    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Input Error",
                text=message,
                buttons=[MDFlatButton(text="EXIT",on_press=self.exit_app), MDRaisedButton(text="CONTINUE",md_bg_color="#ca765b",on_press=self.dismiss_dialog)],
                md_bg_color = "#fff6ee"
            )
        else:
            self.dialog.text = message
        self.dialog.open()

    def dismiss_dialog(self, instance):
        if self.dialog: 
            self.dialog.dismiss()

    def exit_app(self, instance):
        self.stop() 

    def clear_previous_labels(self):
        for label in self.added_labels:
            self.root.remove_widget(label)
        self.added_labels = []

    def on_continue(self):
        try:
            value_f = self.root.ids.input_f.text
            value_alpha = self.root.ids.input_alpha.text
            value_beta = self.root.ids.input_beta.text

            if not value_f or not value_alpha or not value_beta:
                self.show_error_dialog("All input fields must be filled.")
                return

            value_f = int(value_f)
            value_alpha = int(value_alpha)
            value_beta = int(value_beta)

            if value_f < 0 or value_alpha < 0 or value_beta < 0:
                self.show_error_dialog("Inputs must not be negative.")
                return
            
            self.clear_previous_labels()

            self.root.ids.background_image.source = 'Mechanics\\Question1p1.png'

            label_1 = MDLabel(
                text=f"{-round(value_f*sin(radians(value_beta)),3)}N",
                pos_hint={"center_x": 0.845, "center_y": 0.398},
                halign="center",
                font_size = "40sp" ,
                text_color="#ca765b",
                font_name='Kodchasan'
                )
            
            label_2 = MDLabel(
                text=f"{-round(value_f*cos(radians(value_beta)),3)}N",
                pos_hint={"center_x": 0.655, "center_y": 0.35},
                halign="center",
                text_color="#ca765b",
                font_name='Kodchasan' 
                )
            
            label_3 = MDLabel(
                text=f"{round(value_f*sin(radians(value_beta+value_alpha)),3)}N",
                pos_hint={"center_x": 0.775, "center_y": 0.2999},
                halign="center",
                text_color="#ca765b",
                font_name='Kodchasan' 
                )
            
            label_4 = MDLabel(
                text=f"{round(value_f*cos(radians(value_beta+value_alpha)),3)}N",
                pos_hint={"center_x": 0.725, "center_y": 0.25},
                halign="center",
                text_color="#ca765b",
                font_name='Kodchasan' 
                )
            
            self.root.add_widget(label_1)
            self.root.add_widget(label_2)
            self.root.add_widget(label_3)
            self.root.add_widget(label_4)
            self.added_labels.extend([label_1, label_2, label_3, label_4])
        
        except ValueError:
            self.show_error_dialog("Please enter valid numeric values.")

if __name__ == "__main__":
    LabelBase.register(name="Kodchasan", fn_regular="Mechanics\\Kodchasan-Regular.ttf")
    ForceComponentsApp().run()