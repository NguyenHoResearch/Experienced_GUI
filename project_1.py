"""-----What will I learn in this project-----
- 1. What is Tkinter?
- 2. Creating a Basic Tkinter Window
- 3. Adding Widgets (Labels, Buttons, Entry Fields)
- 4. Handling User Events
- 5. Project 1: Simple GUI App
"""
# 1. What is Tkinter?
# Tkinter is Python's standard library for building desktop applications.
# It is easy to use, lightweight, and highly customizable.

# %% Simple GUI Example
import tkinter as tk

# 2. Creating a Basic Tkinter Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("300x200")

# 3. Adding Widgets (Labels, Buttons, Entry Fields)
# Adding lable
lable = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
lable.pack(pady=10)

# Adding Entry
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Adding Button 
def on_click():
    text = entry.get()
    lable.config(text=f"Hello, {text}")

button = tk.Button(root, text="Click Me", command="on_click")

# Run the application
root.mainloop()

# %% 4. Handling User Events
import tkinter as tk
root = tk.Tk()
root. title("Event Handling Example")
root. geometry ("300x200" )

# Add Widgets
label = tk.Label(root, text="Enter your name:")
label.pack()
entry = tk.Entry(root)
entry.pack()
def greet():
    name = entry.get ()
    label. config (text=f"Hello, {name}!")

button = tk. Button(root, text="Greet", command=greet)
button. pack()

root.mainloop ()

# %% 5. Project 1: Simple GUI App
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Welcome to My GUI App!", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=20)

# Name Entry
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg="green")
    else:
        greeting_label.config(text="Please enter your name!", fg="red")

# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")

# Greet Button
greet_button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12), bg="red", fg="blue")
greet_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="red", fg="blue")
reset_button.pack(pady=5)

# Greeting Label
greeting_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
greeting_label.pack(pady=20)

# Run the Application
root.mainloop()

# %%
