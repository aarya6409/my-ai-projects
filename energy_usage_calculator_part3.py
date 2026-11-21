import tkinter as tk
from tkinter import ttk

#define wattage for each appliance
appliance_wattage = {
    "TV": 100,
    "Fridge": 150,
    "Washing Machine": 500,
    "Computer": 200,
    "Fan": 75
}

root = tk.Tk()
root.title("Energy Usage Calculator")
root.geometry("700x550")

appliances = list(appliance_wattage.keys()) #list of appliance names
selected_vars = {} #stores IntVar for each checkbox
hour_entries = {} #stores Entry widget for each appliance

#GUI title
title = tk.Label(root, text="Appliance Energy Usage", font=("Helvetica", 16))
title.pack(pady=10)

#input frame for checkboxes and hours input
input_frame = tk.LabelFrame(root, text="Select Appliances and Enter Usage (hrs/day)", padx=10, pady=10)
input_frame.pack(pady=10, fill='x')

for i, appliance in enumerate(appliances):
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.grid(row=i, column=0, sticky='w', padx=10)

    hour_label = tk.Label(input_frame, text="Hours:")
    hour_label.grid(row=i, column=1, padx=5)

    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=i, column=2)

    selected_vars[appliance] = var
    hour_entries[appliance] = entry

def calculate():
    output_text.delete(1.0, tk.END) #clear previous output
    output_text.insert(tk.END, "Appliance-wise Energy Usage:\n\n")

    total_energy = 0 #initialize total energy variable

    for appliance in appliances:
        if selected_vars[appliance].get() == 1: #if checkbox is selected
            try:
                hours = float(hour_entries[appliance].get())  #get entered hours
                wattage = appliance_wattage[appliance] #get wattage
                energy_kwh = (wattage * hours) / 1000 #convert to kWh
                total_energy += energy_kwh
                output_text.insert(tk.END, f"{appliance}: {hours} hrs ")
            except ValueError:
                output_text.insert(tk.END, f"{appliance}: Invalid input hours!\n")

    output_text.insert(tk.END, f"\nTotal Energy Used Per Day: {total_energy:.2f} kWh")

#calculate button
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.pack(pady=10)

summary_frame = tk.Frame(root)
summary_frame.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(summary_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(summary_frame, height=10, yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(fill="both", expand=True)

scrollbar.config(command=output_text.yview)

#run application
root.mainloop()