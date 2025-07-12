import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        # Variables
        self.current_number = tk.StringVar()
        self.current_number.set("0")
        self.stored_number = 0
        self.current_operation = None
        self.new_number = True

        self.create_widgets()

    def create_widgets(self):
        # Display
        display_frame = tk.Frame(self.window)
        display_frame.pack(pady=10, padx=10, fill="x")

        self.display = tk.Entry(display_frame, textvariable=self.current_number, 
                              font=("Arial", 20), justify="right", bd=5, relief="sunken")
        self.display.pack(fill="x")

        # Buttons frame
        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text:  # Skip empty buttons
                    button = tk.Button(buttons_frame, text=button_text, 
                                     font=("Arial", 14), width=5, height=2,
                                     command=lambda text=button_text: self.button_click(text))
                    button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.handle_number(button_text)
        elif button_text in ['+', '-', '×', '÷']:
            self.handle_operator(button_text)
        elif button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.clear()
        elif button_text == '±':
            self.negate()
        elif button_text == '%':
            self.percentage()

    def handle_number(self, number):
        if self.new_number:
            self.current_number.set(number)
            self.new_number = False
        else:
            if number == '.' and '.' in self.current_number.get():
                return
            current = self.current_number.get()
            if current == '0' and number != '.':
                self.current_number.set(number)
            else:
                self.current_number.set(current + number)

    def handle_operator(self, operator):
        if self.current_operation and not self.new_number:
            self.calculate()
        
        self.stored_number = float(self.current_number.get())
        self.current_operation = operator
        self.new_number = True

    def calculate(self):
        if self.current_operation and not self.new_number:
            current = float(self.current_number.get())
            if self.current_operation == '+':
                result = self.stored_number + current
            elif self.current_operation == '-':
                result = self.stored_number - current
            elif self.current_operation == '×':
                result = self.stored_number * current
            elif self.current_operation == '÷':
                if current == 0:
                    self.current_number.set("Error")
                    return
                result = self.stored_number / current

            self.current_number.set(str(result))
            self.current_operation = None
            self.new_number = True

    def clear(self):
        self.current_number.set("0")
        self.stored_number = 0
        self.current_operation = None
        self.new_number = True

    def negate(self):
        current = float(self.current_number.get())
        self.current_number.set(str(-current))

    def percentage(self):
        current = float(self.current_number.get())
        self.current_number.set(str(current / 100))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
