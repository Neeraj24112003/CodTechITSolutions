import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Define the calculator class
class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg='#1e1e1e')

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 18), padding=10, relief='flat', background='#333', foreground='white')
        self.style.map('TButton', background=[('active', '#555')], relief=[('pressed', 'sunken')])

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        # Display frame for entry and history
        display_frame = tk.Frame(self, bg='#1e1e1e')
        display_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Entry widget for input and result display
        self.entry = tk.Entry(display_frame, font=('Helvetica', 24), borderwidth=0, relief='solid', bg='#1e1e1e', fg='white', insertbackground='white')
        self.entry.pack(fill='both', expand=True, padx=10, pady=(10, 5))

        # Label for showing history/expressions
        self.history_label = tk.Label(display_frame, font=('Helvetica', 14), bg='#1e1e1e', fg='grey', anchor='e')
        self.history_label.pack(fill='both', expand=True, padx=10, pady=(0, 10))

        # Buttons configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('AC', 5, 3)
        ]

        for (text, row, column) in buttons:
            if text == '=':
                ttk.Button(self, text=text, style='TButton', command=self.calculate).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
            elif text == 'C':
                ttk.Button(self, text=text, style='TButton', command=self.clear).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
            elif text == 'AC':
                ttk.Button(self, text=text, style='TButton', command=self.clear_all).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
            else:
                ttk.Button(self, text=text, style='TButton', command=lambda t=text: self.append_character(t)).grid(row=row, column=column, sticky='nsew', padx=5, pady=5)

        # Configure grid weight for responsiveness
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def append_character(self, character):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current_text + character)

    def clear(self):
        self.entry.delete(len(self.entry.get()) - 1, tk.END)

    def clear_all(self):
        self.entry.delete(0, tk.END)
        self.history_label.config(text="")

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.history_label.config(text=expression + "=")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.clear_all()

    def bind_keys(self):
        # Bind keys for numbers, operators, and functions
        for key in "0123456789":
            self.bind(key, lambda e, k=key: self.append_character(k))

        for key in "+-*/().":
            self.bind(key, lambda e, k=key: self.append_character(k))

        self.bind("<Return>", lambda e: self.calculate())
        self.bind("<BackSpace>", lambda e: self.clear())
        self.bind("c", lambda e: self.clear())
        self.bind("<Escape>", lambda e: self.clear_all())

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()
