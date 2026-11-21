import tkinter as tk

root = tk.Tk()
root.title("Name and Age Display")
root.geometry("700x500")

title = tk.Label(root, text="User Info", font=("Helvetica", 16))
title.pack(pady=10)

input_frame = tk.LabelFrame(root, text="Type Name and Age", font=("Arial", 12), padx=10, pady=10)
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)   

age_label = tk.Label(input_frame, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(input_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="Your name and age will appear here.", font=("Arial", 12))
result_label.pack(pady=20)

def display_info():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        result_label.config(text=f"Name: {name}, Age: {age}")
    else:
        result_label.config(text="Please enter both name and age.")

display_button = tk.Button(root, text="Display Info", command=display_info)
display_button.pack(pady=10)

root.mainloop()