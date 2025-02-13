"""-----What will I learn in this Project-----
- 1. Introduction to Advanced Tkinter Widgets
- 2. Using Listbox for Dynamic Lists
- 3. Scrollbar Integration
- 4. Handling User Actions (Add, Delete, Clear)
- 5. Project 6: To-Do List GUI
"""
# %% 1. Introduction to Advanced Tkinter Widgets
# As I mentioned, the Listbox widget, which displays a list of items, can be useful for showing a to-do list in this case.
# Then we have the Scrollbar, which allows scrolling through the content of widgets such as Listbox, Canvas, etc.
# The Frame widget was used in our previous project, where we created a drawing pad. We added a Frame and placed items inside it.
# Frames help organize widgets into sections, using rows and columns as needed.

# %% 2. Using Listbox for Dynamic Lists
# The Listbox widget allows users to add, select, and remove items from a list.  
# It supports multi-selection, scrolling, and dynamic updates.
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Listbox Example")
root.geometry ("300x300")

# Listbox Widget
listbox = tk. Listbox (root)
listbox.pack(pady=10)

# Add Items to Listbox
listbox.insert(tk. END,"Task 1")
listbox.insert(tk. END,"Task 2")

# Get Selected Item
def get_selected():
    selected = listbox.get(tk.ACTIVE)
    print ("Selected:", selected)

button = tk.Button(root, text="Get Selected", command=get_selected)
button.pack(pady=10)

root.mainloop ()

# %% 3. Scrollbar Integration
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Listbox with Scrollbar")
root.geometry ("300x300")

# Frame for Listbox and Scrollbar
frame = tk.Frame (root)
frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar (frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10)
listbox.pack()

# Configure Scrollbar
scrollbar.config(command=listbox.yview)
# Add Items
for i in range(1, 21):
    listbox.insert(tk. END, f"'Item {i}")

root.mainloop()

# %% 4. Handling User Actions (Add, Delete, Clear)
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Listbox Management")
root.geometry ("300x300" )

# Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=10)
# Add Item
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Delete Item
def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Entry Field
entry = tk.Entry(root)
entry.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Item", command=delete_item)
delete_button.pack(pady=5)

root.mainloop ()

# %% 5. Project 6: To-Do List GUI
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#e3f2fd")

# Functions
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Task cannot be empty.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showerror("Error", "Select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 24), bg="#e3f2fd")
title_label.pack(pady=10)

# Entry Field
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4caf50", fg="black")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12), bg="#f44336", fg="black")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, font=("Arial", 12), bg="#607d8b", fg="black")
clear_button.grid(row=0, column=2, padx=5)

# Task Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
task_listbox.pack(pady=10)

scrollbar.config(command=task_listbox.yview)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#d32f2f", fg="black")
exit_button.pack(pady=10)

# Run the App
root.mainloop()

# %%
