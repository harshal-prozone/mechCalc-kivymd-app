from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.core.text import LabelBase
from PIL import Image
from kivymd.uix.dialog import MDDialog
from math import *
from kivymd.uix.button import *
import math

image_path = 'Mechanics\\Question4.png'
image = Image.open(image_path)
Window.size = image.size

KV = '''
FloatLayout:
    Image:
        id:background_image
        source: 'Mechanics\\Question4.png'
        allow_stretch: True
        keep_ratio: False

    MDTextField:
        id: input_a
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
        pos_hint: {"center_x": 0.83, "center_y": 0.73}

    MDTextField:
        id: input_b
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
        pos_hint: {"center_x": 0.83, "center_y": 0.64}

    MDFillRoundFlatButton:
        size_hint: 0.2, 0.07
        md_bg_color: 1, 1, 1, 0
        pos_hint: {"center_x": 0.665, "center_y": 0.508}
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
            mu_s = self.root.ids.input_a.text
            theta = self.root.ids.input_b.text

            if not mu_s or not theta :
                self.show_error_dialog("All input fields must be filled.")
                return

            mu_s= float(mu_s)
            theta = float(theta)

            if mu_s < 0 or theta < 0 :
                self.show_error_dialog("Inputs must not be negative.")
                return
            
            if theta >= 180:
                self.show_error_dialog("Theta should be within the range")
                return
            
            self.clear_previous_labels()

            self.root.ids.background_image.source = 'Mechanics\\Question4p1.png'
            sin_1 = math.sin(math.radians(theta-90))
            cos_1 = math.cos(math.radians(theta-90))
            tan_1 = math.tan(math.radians(theta-90))
            sin_2 = math.sin(math.radians(180-theta))
            cos_2 = math.cos(math.radians(180-theta))
            sin_3 = math.sin(math.radians(theta))
            term1 = mu_s / ((mu_s*sin_1)+cos_1)
            term2 = 1/((mu_s*tan_1)+1)
            term3 = 1
            term4 = sin_3/2
            numerator = (term2 - term3) * sin_2 + term4
            denominator = term1 + (term2 - term3) * cos_2
            tan_theta = numerator/denominator
            theta_ans = math.degrees(math.atan(tan_theta))

            label_1 = MDLabel(
                text=f"{theta_ans}",
                pos_hint={"center_x": 0.84, "center_y": 0.328},
                halign="center",
                font_size = "40sp" ,
                text_color="#ca765b",
                font_name='Kodchasan'
                )
            
            self.root.add_widget(label_1)
            self.added_labels.extend([label_1])
        
        except ValueError:
            self.show_error_dialog("Please enter valid numeric values.")

if __name__ == "__main__":
    LabelBase.register(name="Kodchasan", fn_regular="Mechanics\\Kodchasan-Regular.ttf")
    ForceComponentsApp().run()

