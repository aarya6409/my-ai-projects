import tkinter as tk

def mix_color():

    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    color = f"#{red:02x}{green:02x}{blue:02x}"

    color_preview.config(bg=color)

    root.config(bg=color)

    color_label.config(text=f"Mixed Color: {color.upper()}")

root = tk.Tk()
root.title("Color Mixer Program")
root.geometry("400x500")

red_label = tk.Label(root, text="Red (0-255)")
red_label.pack(pady=5)

red_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                      command=lambda x: mix_color())
red_slider.pack()

green_label = tk.Label(root, text="Green (0-255)")
green_label.pack(pady=5)

green_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                        command=lambda x: mix_color())
green_slider.pack()

blue_label = tk.Label(root, text="Blue (0-255)")
blue_label.pack(pady=5)

blue_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                       command=lambda x: mix_color())
blue_slider.pack()

color_preview = tk.Label(root, bg="black", width=25, height=8)
color_preview.pack(pady=20)

color_label = tk.Label(root, text="Mixed Color: #000000")
color_label.pack(pady=10)

mix_color()

root.mainloop()