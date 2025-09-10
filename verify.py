import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing Pillow for image handling
import math

def calculate_radius_of_gyration():
    try:
        # Base and height of the triangle
        base = float(entry_base.get())
        height = float(entry_height.get())

        # Area of the triangle
        area = 0.5 * base * height

        # Polar moment of inertia about point A (midpoint of hypotenuse)
        I = (1 / 12) * area * (base*2 + height*2)

        # Radius of gyration
        radius_of_gyration = math.sqrt(I / area)

        # Display result
        messagebox.showinfo("Result", f"Radius of Gyration: {radius_of_gyration:.2f} mm")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for base and height.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Radius of Gyration Calculator")

# Load and display the image
try:
    image = Image.open("Mechanics\\triangle.jpg")  # Replace "triangle.png" with your image file path
    image = image.resize((200, 200))   # Resize the image to fit in the application
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=photo)
    label_image.grid(row=1, column=0, columnspan=2, padx=1, pady=1)
except FileNotFoundError:
    messagebox.showerror("Error", "Image file not found. Please make sure 'triangle.png' is in the same directory.")

# Instruction text
instruction_text = (
    "Determine the radius of gyration about a polar axis "
    "through the midpoint A of the hypotenuse of the "
    "right-triangular area. (Hint: Simplify your calculation "
    "by observing the results for a 30 x 40-mm rectangular area.)"
)
label_instruction = tk.Label(root, text=instruction_text, wraplength=300, justify="left", fg="blue")
label_instruction.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Labels and entry widgets
label_base = tk.Label(root, text="Base of Triangle (mm):")
label_base.grid(row=2, column=0, padx=10, pady=5)
entry_base = tk.Entry(root)
entry_base.grid(row=2, column=1, padx=10, pady=5)

label_height = tk.Label(root, text="Height of Triangle (mm):")
label_height.grid(row=3, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_radius_of_gyration)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()