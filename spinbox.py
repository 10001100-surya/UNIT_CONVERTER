import tkinter as tk
from tkinter import messagebox


def convert_value():
    try:
        # Get the selected unit from the Spinbox
        unit = unit_spinbox.get()

        # Get the value from the Entry widget
        value = entry.get()

        # Convert the value to float
        value = float(value)

        # Perform the conversion based on the selected unit
        if unit == "Kilometers":
            result = value * 0.621371  # Convert kilometers to miles
            result_label.config(text=f"{value} Kilometers is {result:.2f} Miles")
        elif unit == "Miles":
            result = value / 0.621371  # Convert miles to kilometers
            result_label.config(text=f"{value} Miles is {result:.2f} Kilometers")
        else:
            messagebox.showerror("Error", "Unknown unit selected.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Unit Conversion")

# Create an Entry widget for user input
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create a Spinbox widget for unit selection
unit_spinbox = tk.Spinbox(root, values=("Kilometers", "Miles"), width=10)
unit_spinbox.pack(pady=10)

# Create a Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_value)
convert_button.pack(pady=10)

# Create a Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
