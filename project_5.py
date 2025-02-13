"""-----What will I learn in this Project-----
- 1. What are Message Boxes?
- 2. Types of Message Boxes
- 3. Using Message Boxes for Validation
- 4. Handling User Authentication
- 5. Project 5: Simple Login System
"""
# %% 1. What are Message Boxes?
# Message boxes are pop-up dialogs used to display messages, warnings, or confirmation prompts.
# Tkinter provides them through the Messagebox module, which you may have already encountered.
# Common uses include displaying error messages, showing success notifications, or asking for user confirmation.
from tkinter import messagebox
messagebox.showinfo("Title", "This is an information message")

# %% 2. Types of Message Boxes
from tkinter import messagebox 
import tkinter as tk

# Main Window
root = tk.Tk()
root.withdraw()

# Hides the main window
# Show different message boxes
messagebox.showinfo("Info", "This is an info message.") 
messagebox.showwarning ("Warning", "This is a warning message.") 
messagebox.showerror ("Error", "This is an error message.")

response = messagebox.askyesno ("Question", "Do you want to continue?")
print ("Response:", response)

# %% 3. Using Message Boxes for Validation
import tkinter as tk 
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Validation Example")
root.geometry ("300x200")

# Input Field
entry = tk.Entry (root)
entry.pack(pady=10)

# Validate Input
def validate_input():
    user_input = entry.get()
    if user_input.strip() == "":
        messagebox.showerror ("Error", "Input cannot be empty!") 
    else:
        messagebox.showinfo ("Success", f"'You entered: {user_input}")
# Button
button = tk.Button(root, text="Submit", command=validate_input)
button.pack(pady=10)

root.mainloop()

# %% 4. Handling User Authentication
import tkinter as tk 
from tkinter import messagebox

# Main Window
root = tk.Tk()
root. title("Simple Login")
root. geometry ("300x200")

# User Credentials
USERNAME = "admin"
PASSWORD = "NguyenHo"

# Labels and Entry Fields
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Authentication Function
def login():
    username = username_entry.get()
    password = password_entry.get ()
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome, Admin!") 
    else:
        messagebox.showerror ("Login Failed", "Invalid username or password.")

# Login Button
login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack(pady=10)

root.mainloop()

# %% 5. Project 5: Simple Login System
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x300")
root.configure(bg="#f0f4c3")

# Predefined Credentials
USER_CREDENTIALS = {
    "admin": "NguyenHo",
    "user": "NguyenV.Ho"
}

# Title Label
title_label = tk.Label(root, text="Login System", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

# Username Input
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f4c3")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

# Password Input
password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f4c3")
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Clear Function
def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Buttons
login_button = tk.Button(root, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="black")
login_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 12), bg="#f44336", fg="black")
clear_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="#607d8b", fg="black")
exit_button.pack(pady=10)

# Run the App
root.mainloop()













# %%
