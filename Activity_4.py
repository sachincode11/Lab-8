from tkinter import *
from tkinter import messagebox
import json
import os

FILE_NAME = "login.json"

# Load users
def load_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save users
def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

# Register Window
def open_register():
    def register_user():
        username = entry_user.get()
        password = entry_pass.get()
        confirm = entry_confirm.get()

        users = load_users()

        # Check if user exists
        for user in users:
            if user["username"] == username:
                messagebox.showerror("Error", "User already exists!")
                return

        if not username or not password:
            messagebox.showwarning("Error", "All fields required!")
            return

        if password != confirm:
            messagebox.showwarning("Error", "Passwords do not match!")
            return

        # Add user
        users.append({
            "username": username,
            "password": password
        })

        save_users(users)
        messagebox.showinfo("Success", "Registration successful!")
        reg_window.destroy()

    reg_window = Toplevel(root)
    reg_window.title("Register")

    Label(reg_window, text="Username").grid(row=0, column=0)
    entry_user = Entry(reg_window)
    entry_user.grid(row=0, column=1)

    Label(reg_window, text="Password").grid(row=1, column=0)
    entry_pass = Entry(reg_window, show="*")
    entry_pass.grid(row=1, column=1)

    Label(reg_window, text="Confirm Password").grid(row=2, column=0)
    entry_confirm = Entry(reg_window, show="*")
    entry_confirm.grid(row=2, column=1)

    Button(reg_window, text="OK", command=register_user).grid(row=3, column=0)
    Button(reg_window, text="Cancel", command=reg_window.destroy).grid(row=3, column=1)

# Login Function
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            messagebox.showinfo("Success", "Login Successful!")
            return

    messagebox.showerror("Error", "User not found! Please register.")

# MAIN GUI
root = Tk()
root.title("Login System")
root.geometry("300x200")

Label(root, text="Username").grid(row=0, column=0, pady=10)
entry_username = Entry(root)
entry_username.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
entry_password = Entry(root, show="*")
entry_password.grid(row=1, column=1)

Button(root, text="Login", width=10, command=login_user).grid(row=2, column=0, pady=10)
Button(root, text="Register", width=10, command=open_register).grid(row=2, column=1)

root.mainloop()