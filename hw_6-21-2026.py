import tkinter as tk
from tkinter import messagebox

foods = {
    "Apple": 95,
    "Burger": 300,
    "Milk": 120,
    "Rice": 200,
    "Salad": 80
}

root = tk.Tk()
root.title("Healthy Meal Planner")
root.geometry("400x500")

food_vars = {}
qty_vars = {}

title = tk.Label(root, text="Select food items & quantity:", font=("Arial", 12, "bold"))
title.pack(pady=10)

for food, calories in foods.items():
    frame = tk.Frame(root)
    frame.pack(anchor="w", padx=20, pady=5)

    var = tk.IntVar()
    food_vars[food] = var

    cb = tk.Checkbutton(
        frame,
        text=f"{food} ({calories} kcal each)",
        variable=var
    )
    cb.pack(side="left")

    tk.Label(frame, text="Qty:").pack(side="left", padx=5)

    qty = tk.StringVar(value="1")
    qty_vars[food] = qty

    entry = tk.Entry(frame, width=5, textvariable=qty)
    entry.pack(side="left")

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=15)

feedback_label = tk.Label(root, text="", font=("Arial", 11))
feedback_label.pack()

suggestion_label = tk.Label(root, text="", fg="green", font=("Arial", 10))
suggestion_label.pack(pady=10)

def calculate_meal():
    total = 0

    try:
        for food, calories in foods.items():
            if food_vars[food].get() == 1:
                quantity = int(qty_vars[food].get())
                total += calories * quantity

        result_label.config(text=f"Total Calories: {total} kcal")

        if total <= 800:
            feedback_label.config(
                text="Healthy Meal!",
                fg="green"
            )
            suggestion_label.config(text="")
        else:
            feedback_label.config(
                text="This meal is not so healthy.",
                fg="red"
            )

            suggestions = []

            if food_vars["Burger"].get():
                suggestions.append("Swap Burger with Grilled Veggie Wrap")

            if food_vars["Milk"].get():
                suggestions.append("Swap Milk with Almond Milk")

            if not suggestions:
                suggestions.append("Add more fruits and vegetables")

            suggestion_label.config(
                text="Suggestions:\n" + "\n".join(suggestions)
            )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid quantities."
        )

calc_btn = tk.Button(
    root,
    text="Calculate Meal",
    command=calculate_meal,
    bg="lightblue"
)
calc_btn.pack(pady=10)

root.mainloop()
