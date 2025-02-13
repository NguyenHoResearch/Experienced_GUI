"""-----What will I learn in this project-----
- 1. Understanding Input Fields in Tkinter
- 2. Getting and Validating User Input
- 3. Displaying Dynamic Results
- 4. Using Entry Widgets with Labels and Buttons
- 5. Project 3: BMI Calculator
"""
# %% 1. Understanding Input Fields in Tkinter
# Tkinter, entry widgets are used for single line text input, which we have seen earlier.
# They are ideal for accepting user data like numbers, names and other textual input.
import tkinter as tk

# Main Window
root = tk.Tk()
root. title("Input Field Example")
root. geometry ("300x200")

# Input Field
entry = tk. Entry(root, width=25)
entry. pack(pady=10)

# Button to Display Input
def display_input():
    user_input = entry.get()
    print ("User Input:", user_input)

button = tk.Button(root, text="Submit", command=display_input)
button.pack(pady=10)

# Run Application
root.mainloop()

# %% 2. Getting and Validating User Input
import tkinter as tk
root = tk.Tk()
root. title("Input Validation")
root. geometry ("300x200")

# Input Field
entry = tk. Entry(root)
entry.pack(pady=10)

# Validate Input
def validate_input():
    try:
        value = float(entry.get())
        print(f"✅ Valid Input: {value}")
    except ValueError:
        print("❌ Invalid Input. Please enter a number.")

button = tk. Button(root, text="Validate", command=validate_input)
button. pack(pady=10)

root.mainloop ()

# %% 3. Displaying Dynamic Results
import tkinter as tk
root = tk. Tk()
root. title("Dynamic Result Display")
root. geometry ("300x200")

# Input Field
entry = tk. Entry(root)
entry.pack(pady=10)

# Result Label
result_label = tk. Label(root, text="Result will be displayed here.")
result_label.pack(pady=10)

# Update Label
def update_label ():
    text = entry.get()
    result_label. config (text=f"You entered: {text}")

button = tk. Button(root, text="Update", command=update_label)
button. pack(pady=10)
root.mainloop()
 
# %% 4. Using Entry Widgets with Labels and Buttons
# From 3, Now combining entry fields, labels and buttons is key to building functional user interfaces.
# Now best practices that you that you need to follow is first validate user input before processing.
# Provide feedback via labels and use default values or placeholders in entry widgets.

# %% 5. Project 3: BMI Calculator 
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#f0f4c3")

# Title Label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Weight Input
weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12), bg="#f0f4c3")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack(pady=5)

# Height Input
height_label = tk.Label(root, text="Enter your height (m):", font=("Arial", 12), bg="#f0f4c3")
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4c3")
result_label.pack(pady=20)

# Calculate BMI Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight / (height ** 2)
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obesity"
        
        result_label.config(text=f"BMI: {bmi:.2f}\nStatus: {status}", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Buttons
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 12), bg="#4caf50", fg="black")
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")], font=("Arial", 12), bg="#f44336", fg="black")
reset_button.pack(pady=5)

# Run the App
root.mainloop()
# %%
