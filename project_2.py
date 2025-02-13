"""-----What will I learn in this project-----
- 1. How Buttons Work in Tkinter
- 2. Binding Events to Buttons
- 3. Dynamic Updates Using Button Events
- 4. Managing Button States
- 5. Project 2: Click Counter App
"""
#%% # %% 1. How Buttons Work in Tkinter
# Buttons are widgets in Tkinter that trigger an event handler when clicked.
# Events can call functions, update variables, or modify other widgets. 
# The command parameter in a button links it to a specific function.

#%% 2. Binding Events to Buttons
import tkinter as tk
root = tk.Tk()
root.title("Button Events")
root.geometry ("300x200" )

# Event Handlers
def on_enter(event):
    button.config(text="Mouse Over")

def on_leave(event) :
    button.config(text="Mouse Out")

# Create Button
button = tk.Button(root, text="Hover Me")
button. pack(pady=20)

# Bind Events
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()

#%% 3. Dynamic Updates Using Button Events
import tkinter as tk
root = tk.Tk()

root.title("Dynamic Button Counter")
root.geometry ("300x200" )

# Counter Variable
counter = 0
def increment_counter():
    global counter 
    counter += 1
    label.config(text=f"Count: {counter}")

# Label and Button
label = tk.Label(root, text="Count: 0", font=("Arial", 14))
label. pack(pady=10)
button = tk.Button(root, text="Ctick Me", command=increment_counter)
button. pack(pady=10)
root.mainloop ()

#%% 4. Managing Button States
import tkinter as tk
root = tk.Tk()
root.title("Button State Management")
root.geometry ("300x200")

def toggle_button():
    if button["state"] == "normal":
        button.config(state="disabled")
        toggle_btn.config(text="Enable Button")
    else:
        button.config(state='normal' )
        toggle_btn.config(text="Disable Button" )

# Buttons
button = tk.Button(root, text="I am Active")
button.pack(pady=10)

toggle_btn = tk.Button(root, text="Disable Button", command=toggle_button)
toggle_btn.pack(pady=10)

root.mainloop ( )

# %% 5. Project 2: Click Counter App
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Click Counter App")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

# Counter Variable
counter = 0

# Increment Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

# Reset Function
def reset():
    global counter
    counter = 0
    counter_label.config(text="Clicks: 0")

# Title Label
title_label = tk.Label(root, text="Click Counter", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=20)

# Counter Label
counter_label = tk.Label(root, text="Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

# Increment Button
increment_button = tk.Button(root, text="Click Me", command=increment, font=("Arial", 14), bg="#4caf50", fg="black")
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 14), bg="#f44336", fg="black")
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14), bg="#607d8b", fg="black")
exit_button.pack(pady=10)

# Run the App
root.mainloop()

# %%
