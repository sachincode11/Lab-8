import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class TemperatureConverterApp:
    def __init__(self, root):
        if root is None:
            return # allow testing without GUI
        
        self.root = root
        self.root.title('Temperature Converter')
        self.root.geometry('320x100')
        self.root.resizable(False, False)

        # main frame
        self.frame = ttk.Frame(self.root)
        self.frame.grid(padx=10, pady=10)

        # options
        self.options = {'padx': 5, 'pady': 5}

        # variable
        self.temperature = tk.StringVar()

        # UI setup
        self.create_widgets()

    # Create Widgets
    def create_widgets(self):
        # Label
        ttk.Label(self.frame, text='Fahrenheit').grid(
            column=0, row=0, sticky='W', **self.options)

        # Entry
        self.temperature_entry = ttk.Entry(
            self.frame, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **self.options)
        self.temperature_entry.focus()

        # Button
        ttk.Button(
            self.frame,
            text='Convert',
            command=self.convert
        ).grid(column=2, row=0, sticky='W', **self.options)

        # Result Label
        self.result_label = ttk.Label(self.frame)
        self.result_label.grid(row=1, columnspan=3, **self.options)

    # Conversion Logic
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

    # Event Handler
    def convert(self):
        try:
            f = float(self.temperature.get())
            c = self.fahrenheit_to_celsius(f)
            result = f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()