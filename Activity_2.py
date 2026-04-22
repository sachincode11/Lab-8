from tkinter import *

# Create main window
root = Tk()
root.title("Programming Languages Selector")
root.geometry("500x300")

# Listbox + Scrollbar
scrollbar_list = Scrollbar(root)
scrollbar_list.grid(row=0, column=1, sticky='ns', padx=(0,10), pady=10)

listbox = Listbox(root, height=10, width=20, yscrollcommand=scrollbar_list.set)

languages = [
    "Python", "Java", "C++", "JavaScript", "Go",
    "Rust", "Kotlin", "Swift", "PHP", "Ruby",
    "TypeScript", "Dart"
]

for lang in languages:
    listbox.insert(END, lang)

listbox.grid(row=0, column=0, padx=10, pady=10)
scrollbar_list.config(command=listbox.yview)

# Text Widget + Scrollbar
scrollbar_text = Scrollbar(root)
scrollbar_text.grid(row=0, column=3, sticky='ns', padx=(0,10), pady=10)

text_area = Text(root, height=10, width=25, yscrollcommand=scrollbar_text.set)
text_area.grid(row=0, column=2, padx=10, pady=10)

scrollbar_text.config(command=text_area.yview)

# Function to display selection
def show_selected():
    if listbox.curselection():
        selected = listbox.get(listbox.curselection())
        text_area.delete(1.0, END)
        text_area.insert(END, selected)
        print("Selected:", selected)

# Button
btn = Button(root, text="Show Selection", command=show_selected)
btn.grid(row=1, column=1, pady=10)

# Bind event (auto display on click)
def on_select(event):
    show_selected()

listbox.bind("<<ListboxSelect>>", on_select)

# Run application
root.mainloop()