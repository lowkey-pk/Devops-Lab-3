import tkinter as tk
from tkinter import messagebox

# Function to validate registration
def register_user():
    userid = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if userid == "" or password == "" or confirm_password == "":
        messagebox.showwarning("Registration Failed", "All fields are required.")
    elif password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match.")
    else:
        # You can add code here to save the user details
        messagebox.showinfo("Registration Successful", f"User '{userid}' registered successfully!")

# Create the main window
parent = tk.Tk()
parent.title("Registration Form")

# User ID
username_label = tk.Label(parent, text="User ID:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Password
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")
password_entry.pack()

# Confirm Password
confirm_password_label = tk.Label(parent, text="Confirm Password:")
confirm_password_label.pack()

confirm_password_entry = tk.Entry(parent, show="*")
confirm_password_entry.pack()

# Register Button
register_button = tk.Button(parent, text="Register", command=register_user)
register_button.pack(pady=10)

# Start the Tkinter event loop
parent.mainloop()