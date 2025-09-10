from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.core.text import LabelBase
from PIL import Image
from kivymd.uix.dialog import MDDialog
from math import *
from kivymd.uix.button import *
image_path = 'Mechanics\\Question2.png'
image = Image.open(image_path)
Window.size = image.size

KV = '''
FloatLayout:
    Image:
        id:background_image
        source: 'Mechanics\\Question2.png'
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
        pos_hint: {"center_x": 0.8, "center_y": 0.785}

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
        pos_hint: {"center_x": 0.8, "center_y": 0.699}

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
        pos_hint: {"center_x": 0.8, "center_y": 0.6}

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
        pos_hint: {"center_x": 0.8, "center_y": 0.51}

    MDFillRoundFlatButton:
        size_hint: 0.2, 0.07
        md_bg_color: 1, 1, 1, 0
        pos_hint: {"center_x": 0.665, "center_y": 0.385}
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

            if not value_a or not value_b or not value_c or not value_h:
                self.show_error_dialog("All input fields must be filled.")
                return

            value_a = int(value_a)
            value_b = int(value_b)
            value_c = int(value_c)
            value_h = int(value_h)

            if value_a < 0 or value_b < 0 or value_c < 0 or value_h < 0 :
                self.show_error_dialog("Inputs must not be negative.")
                return
            
            self.clear_previous_labels()

            self.root.ids.background_image.source = 'Mechanics\\Question2p1.png'
            I_x1 = ((value_c)**3 * (2*value_a+2*value_b))/3
            if value_c<=value_h:
                I_x = I_x1
            else:
                a=((2*value_b)*(value_b**3))/12
                if value_c<=value_h+value_b:
                    value_d=-(value_h-value_c)
                    print(value_d)
                else:
                    value_d=value_b

                b=(2*value_b*value_d)*(value_h+(value_d/2))**2
                print(b)
                I_x2 = a+b
                I_x= I_x1 - I_x2

            label_1 = MDLabel(
                text=f"{I_x}N",
                pos_hint={"center_x": 0.8499, "center_y": 0.2347},
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