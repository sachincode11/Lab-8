import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

root = tk.Tk()
root.title("Favourite Language")
root.geometry("600x420")

FILE_NAME = "data.json"

# Load Data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        records = json.load(f)
else:
    records = []

current_index = -1

# Helper Functions
def save_to_file():
    with open(FILE_NAME, "w") as f:
        json.dump(records, f, indent=4)

def get_form_data():
    return {
        "name": name_entry.get(),
        "city": city_entry.get(),
        "python": python_var.get(),
        "java": java_var.get(),
        "comments": comments_text.get("1.0", tk.END).strip(),
        "archived": False
    }

def load_record(index):
    if 0 <= index < len(records):
        rec = records[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, rec["name"])

        city_entry.delete(0, tk.END)
        city_entry.insert(0, rec["city"])

        python_var.set(rec["python"])
        java_var.set(rec["java"])

        comments_text.delete("1.0", tk.END)
        comments_text.insert(tk.END, rec["comments"])

# Button Functions 
def save_record():
    global current_index
    data = get_form_data()
    records.append(data)
    current_index = len(records) - 1
    save_to_file()
    messagebox.showinfo("Saved", "Record saved to JSON")

def clear_form():
    name_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    python_var.set(False)
    java_var.set(False)
    comments_text.delete("1.0", tk.END)

def delete_record():
    global current_index
    if 0 <= current_index < len(records):
        records.pop(current_index)
        save_to_file()
        current_index -= 1
        clear_form()
        messagebox.showinfo("Deleted", "Record deleted")
    else:
        messagebox.showwarning("Warning", "No record selected")

def archive_record():
    if 0 <= current_index < len(records):
        records[current_index]["archived"] = True
        save_to_file()
        messagebox.showinfo("Archived", "Record archived")
    else:
        messagebox.showwarning("Warning", "No record selected")

def next_record():
    global current_index
    if current_index < len(records) - 1:
        current_index += 1
        load_record(current_index)

def prev_record():
    global current_index
    if current_index > 0:
        current_index -= 1
        load_record(current_index)

def save_comments():
    if 0 <= current_index < len(records):
        records[current_index]["comments"] = comments_text.get("1.0", tk.END).strip()
        save_to_file()
        messagebox.showinfo("Saved", "Comments updated")
    else:
        messagebox.showwarning("Warning", "No record selected")

# UI Layout
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(main_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = ttk.Entry(main_frame, width=30)
name_entry.grid(row=0, column=1)

ttk.Label(main_frame, text="City:").grid(row=1, column=0, sticky="w")
city_entry = ttk.Entry(main_frame, width=30)
city_entry.grid(row=1, column=1)

python_var = tk.BooleanVar()
java_var = tk.BooleanVar()

ttk.Checkbutton(main_frame, text="Python", variable=python_var).grid(row=2, column=1, sticky="w")
ttk.Checkbutton(main_frame, text="Java", variable=java_var).grid(row=3, column=1, sticky="w")

# Buttons
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=0, column=2, rowspan=4, padx=20)

ttk.Button(button_frame, text="Save", width=12, command=save_record).grid(row=0, column=0, pady=2)
ttk.Button(button_frame, text="Clear", width=12, command=clear_form).grid(row=1, column=0, pady=2)
ttk.Button(button_frame, text="Delete", width=12, command=delete_record).grid(row=2, column=0, pady=2)
ttk.Button(button_frame, text="Archive", width=12, command=archive_record).grid(row=3, column=0, pady=2)

ttk.Button(button_frame, text="Next", width=12, command=next_record).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="Previous", width=12, command=prev_record).grid(row=1, column=1, padx=10)
ttk.Button(button_frame, text="Close", width=12, command=root.quit).grid(row=2, column=1, padx=10)

# Comments
ttk.Label(main_frame, text="Comments:").grid(row=4, column=0, columnspan=3, sticky="w", pady=(10,0))

comments_text = tk.Text(main_frame, height=8)
comments_text.grid(row=5, column=0, columnspan=3, sticky="nsew")

ttk.Button(main_frame, text="Save Comments", command=save_comments).grid(row=6, column=0, sticky="w")

# Layout config
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

root.mainloop()