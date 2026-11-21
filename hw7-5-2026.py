import tkinter as tk
from tkinter import ttk

products = {
    "Book": 10,
    "Toy": 15,
    "Snacks": 5,
    "Pencil": 2
}

def calculate_total():
    for item in tree.get_children():
        tree.delete(item)

    total = 0

    for product, price in products.items():
        if product_vars[product].get():

            try:
                quantity = int(quantity_entries[product].get())
                if quantity < 1:
                    quantity = 1
            except ValueError:
                quantity = 1

            item_total = price * quantity
            total += item_total

            tree.insert(
                "",
                "end",
                values=(product, quantity, f"${price:.2f}", f"${item_total:.2f}")
            )

    total_label.config(text=f"Total Amount: ${total:.2f}")

root = tk.Tk()
root.title("Shopping Cart Calculator 🛒")
root.geometry("550x450")

title = tk.Label(
    root,
    text="Shopping Cart Calculator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

product_vars = {}
quantity_entries = {}

for product, price in products.items():
    row = tk.Frame(input_frame)
    row.pack(anchor="w", pady=2)

    var = tk.BooleanVar()
    product_vars[product] = var

    check = tk.Checkbutton(
        row,
        text=f"{product} (${price})",
        variable=var
    )
    check.pack(side="left")

    tk.Label(row, text="Qty:").pack(side="left", padx=5)

    qty_entry = tk.Entry(row, width=5)
    qty_entry.insert(0, "1")
    qty_entry.pack(side="left")

    quantity_entries[product] = qty_entry

calc_button = tk.Button(
    root,
    text="Calculate Total",
    command=calculate_total
)
calc_button.pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=("Item", "Quantity", "Price", "Total"),
    show="headings",
    height=8
)

tree.heading("Item", text="Item")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.heading("Total", text="Item Total")

tree.column("Item", width=120)
tree.column("Quantity", width=80)
tree.column("Price", width=100)
tree.column("Total", width=120)

tree.pack(pady=10)

total_label = tk.Label(
    root,
    text="Total Amount: $0.00",
    font=("Arial", 12, "bold")
)
total_label.pack(pady=10)

root.mainloop()