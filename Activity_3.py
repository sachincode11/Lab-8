from tkinter import *
from tkinter import messagebox
import json

# Load data from JSON
def load_data():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except:
        return []

# Save data to JSON
def save_data():
    with open("users.json", "w") as file:
        json.dump(staff_list, file, indent=4)
    messagebox.showinfo("Success", "Data saved successfully!")

# Display data in Listbox
def refresh_list():
    listbox.delete(0, END)
    for staff in staff_list:
        listbox.insert(END, staff["name"])

# Show details
def show_details(event):
    if listbox.curselection():
        index = listbox.curselection()[0]
        staff = staff_list[index]

        text_area.delete(1.0, END)
        text_area.insert(END,
            f"Name: {staff['name']}\n"
            f"Age: {staff['age']}\n"
            f"Role: {staff['role']}"
        )

# Add new staff window
def add_staff():
    def save_new():
        name = entry_name.get()
        age = entry_age.get()
        role = entry_role.get()

        if name and age and role:
            staff_list.append({
                "name": name,
                "age": age,
                "role": role
            })
            refresh_list()
            add_window.destroy()
        else:
            messagebox.showwarning("Error", "All fields required!")

    add_window = Toplevel(root)
    add_window.title("Add Staff")

    Label(add_window, text="Name").grid(row=0, column=0)
    entry_name = Entry(add_window)
    entry_name.grid(row=0, column=1)

    Label(add_window, text="Age").grid(row=1, column=0)
    entry_age = Entry(add_window)
    entry_age.grid(row=1, column=1)

    Label(add_window, text="Role").grid(row=2, column=0)
    entry_role = Entry(add_window)
    entry_role.grid(row=2, column=1)

    Button(add_window, text="Add", command=save_new).grid(row=3, column=0, columnspan=2)

# Remove staff
def remove_staff():
    if listbox.curselection():
        index = listbox.curselection()[0]
        del staff_list[index]
        refresh_list()
        text_area.delete(1.0, END)
    else:
        messagebox.showwarning("Error", "Select a staff to remove")

# MAIN GUI
root = Tk()
root.title("Staff Management System")
root.geometry("500x300")

staff_list = load_data()

# Listbox
listbox = Listbox(root, width=25)
listbox.grid(row=0, column=0, padx=10, pady=10)

listbox.bind("<<ListboxSelect>>", show_details)

# Text Area
text_area = Text(root, width=30, height=10)
text_area.grid(row=0, column=1, padx=10, pady=10)

# Buttons
Button(root, text="Add", width=10, command=add_staff).grid(row=1, column=0)
Button(root, text="Remove", width=10, command=remove_staff).grid(row=2, column=0)
Button(root, text="Save", width=10, command=save_data).grid(row=3, column=0)

# Load initial data
refresh_list()

root.mainloop()