import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("320x280")

from_unit = ttk.Combobox(
    window,
    width=15,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    state="readonly"
)
from_unit.grid(
    row=0,
    column=0,
    pady=40
)

to_unit = ttk.Combobox(
    window,
    width=15,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    state="readonly"
)
to_unit.grid(
    row=1,
    column=0,
    padx=20,
    pady=40
)

user_entry = tk.Entry(
    window,
    width=15
)
user_entry.grid(
    row=0,
    column=1
)

result_entry = tk.Entry(
    window,
    width=15,
    state="readonly"
)
result_entry.grid(
    row=1,
    column=1
)

def formula(unit1, unit2, data_input):
    if unit1 == "Celsius":
        if unit2 == "Celsius":
            return data_input
        elif unit2 == "Kelvin":
            return data_input + 273.15
        elif unit2 == "Fahrenheit":
            return data_input * 1.8 + 32
    elif unit1 == "Kelvin":
        if unit2 == "Celsius":
            return data_input - 273.15
        elif unit2 == "Kelvin":
            return data_input
        elif unit2 == "Fahrenheit":
            return (data_input - 273.15) * 1.8 + 32
    elif unit1 == "Fahrenheit":
        if unit2 == "Celsius":
            return (data_input - 32) / 1.8
        elif unit2 == "Kelvin":
            return (data_input - 32) / 1.8 + 273.15
        elif unit2 == "Fahrenheit":
            return data_input

def convert_unit():
    data_entry = user_entry.get()

    try:
        result = round(formula(from_unit.get(), to_unit.get(), float(data_entry)), 3)
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
        result_entry.config(state="readonly")
    except:
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid Entry")
        result_entry.config(state="readonly")

convert_button = ttk.Button(
    window,
    text="CONVERT",
    width=15,
    command=convert_unit
).grid(
    row=2,
    column=0,
    columnspan=2
)

window.mainloop()