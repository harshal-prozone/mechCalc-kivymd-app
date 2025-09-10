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

image_path = 'Mechanics\\Question3.png'
image = Image.open(image_path)
Window.size = image.size

KV = '''
FloatLayout:
    Image:
        id:background_image
        source: 'Mechanics\\Question3.png'
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
        pos_hint: {"center_x": 0.85, "center_y": 0.83}

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
        pos_hint: {"center_x": 0.85, "center_y": 0.75}

    MDTextField:
        id: input_c
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
        pos_hint: {"center_x": 0.85, "center_y": 0.67}

    MDTextField:
        id: input_h
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
        pos_hint: {"center_x": 0.85, "center_y": 0.59}

    MDTextField:
        id: input_d
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
        pos_hint: {"center_x": 0.85, "center_y": 0.51}

    MDTextField:
        id: input_e
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
        pos_hint: {"center_x": 0.85, "center_y": 0.43}

    MDFillRoundFlatButton:
        size_hint: 0.2, 0.07
        md_bg_color: 1, 1, 1, 0
        pos_hint: {"center_x": 0.665, "center_y": 0.315}
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
            value_a = self.root.ids.input_a.text
            value_b = self.root.ids.input_b.text
            value_c = self.root.ids.input_c.text
            value_h = self.root.ids.input_h.text
            value_d = self.root.ids.input_d.text
            value_e = self.root.ids.input_e.text

            if not value_a or not value_b or not value_c or not value_h:
                self.show_error_dialog("All input fields must be filled.")
                return

            L_AE = float(value_a)
            L_EG = float(value_b)
            L_EB = float(value_c)
            L_EE_prime = float(value_h)
            m_f = float(value_d)
            m_w = float(value_e)


            if L_AE < 0 or L_EB < 0 or L_EE_prime < 0 or L_EG < 0 or m_f < 0 or m_w < 0 :
                self.show_error_dialog("Inputs must not be negative.")
                return
            
            self.clear_previous_labels()
            self.root.ids.background_image.source = 'Mechanics\\Question3p1.png'
            alpha = math.degrees(math.atan(L_AE / L_EE_prime))
            alpha_rad = math.radians(alpha)
            F = ((m_f * 9.81 * L_EG) + (m_w * 9.81 * L_EB)) / (math.cos(alpha_rad) * L_AE)
            E_x = F * math.sin(alpha_rad)
            E_y = -(F * math.cos(alpha_rad) - (m_f * 9.81) - (m_w * 9.81))
            E = math.sqrt(E_x**2 + E_y**2)
            label_1 = MDLabel(
                text=f"{F}N",
                pos_hint={"center_x": 0.8, "center_y": 0.25},
                halign="center",
                font_size = "40sp" ,
                text_color="#ca765b",
                font_name='Kodchasan'
                )
            label_2 = MDLabel(
                text=f"{E}N",
                pos_hint={"center_x": 0.73, "center_y": 0.19},
                halign="center",
                font_size = "40sp" ,
                text_color="#ca765b",
                font_name='Kodchasan'
                )
            
            self.root.add_widget(label_1)
            self.root.add_widget(label_2)
            self.added_labels.extend([label_1])
        
        except ValueError:
            self.show_error_dialog("Please enter valid numeric values.")

if __name__ == "__main__":
    LabelBase.register(name="Kodchasan", fn_regular="Mechanics\\Kodchasan-Regular.ttf")
    ForceComponentsApp().run()