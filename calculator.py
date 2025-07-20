import tkinter as tk
from tkinter import ttk
import math
import numpy as np

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x700")
        self.current_input = ""
        self.memory = 0
        self.setup_ui()
        
    def setup_ui(self):
        # Display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            self.root, 
            textvariable=self.display_var, 
            font=('Arial', 24), 
            justify='right'
        )
        self.display.pack(fill='x', padx=10, pady=10, ipady=10)
        
        # Memory display
        self.memory_var = tk.StringVar()
        memory_label = ttk.Label(
            self.root, 
            textvariable=self.memory_var, 
            font=('Arial', 10)
        )
        memory_label.pack(anchor='e', padx=10)
        
        # Notebook for different calculator modes
        self.notebook = ttk.Notebook(self.root)
        
        # Standard Calculator Tab
        self.standard_frame = ttk.Frame(self.notebook)
        self.create_standard_buttons()
        
        # Scientific Calculator Tab
        self.scientific_frame = ttk.Frame(self.notebook)
        self.create_scientific_buttons()
        
        # Programming Calculator Tab
        self.programming_frame = ttk.Frame(self.notebook)
        self.create_programming_buttons()
        
        # Conversion Tab
        self.conversion_frame = ttk.Frame(self.notebook)
        self.create_conversion_buttons()
        
        self.notebook.add(self.standard_frame, text="Standard")
        self.notebook.add(self.scientific_frame, text="Scientific")
        self.notebook.add(self.programming_frame, text="Programming")
        self.notebook.add(self.conversion_frame, text="Conversion")
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)
        
    def create_standard_buttons(self):
        buttons = [
            ('MC', 'MR', 'MS', 'M+', 'M-'),
            ('C', '⌫', '%', '÷'),
            ('7', '8', '9', '×'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('±', '0', '.', '='),
        ]
        
        for row in buttons:
            frame = ttk.Frame(self.standard_frame)
            frame.pack(fill='x', padx=2, pady=2)
            for text in row:
                if text == '=':
                    btn = ttk.Button(frame, text=text, command=lambda t=text: self.on_button_click(t))
                    btn.pack(side='left', expand=True, fill='x', ipady=20)
                else:
                    btn = ttk.Button(frame, text=text, command=lambda t=text: self.on_button_click(t))
                    btn.pack(side='left', expand=True, fill='x')

    def create_scientific_buttons(self):
        # First row
        frame1 = ttk.Frame(self.scientific_frame)
        frame1.pack(fill='x', padx=2, pady=2)
        for text in ['sin', 'cos', 'tan', 'π', 'e']:
            btn = ttk.Button(frame1, text=text, command=lambda t=text: self.on_scientific_click(t))
            btn.pack(side='left', expand=True, fill='x')
        
        # Second row
        frame2 = ttk.Frame(self.scientific_frame)
        frame2.pack(fill='x', padx=2, pady=2)
        for text in ['asin', 'acos', 'atan', 'x²', 'x³']:
            btn = ttk.Button(frame2, text=text, command=lambda t=text: self.on_scientific_click(t))
            btn.pack(side='left', expand=True, fill='x')
            
        # Third row
        frame3 = ttk.Frame(self.scientific_frame)
        frame3.pack(fill='x', padx=2, pady=2)
        for text in ['log', 'ln', '√', 'x^y', '10^x']:
            btn = ttk.Button(frame3, text=text, command=lambda t=text: self.on_scientific_click(t))
            btn.pack(side='left', expand=True, fill='x')
            
        # Fourth row
        frame4 = ttk.Frame(self.scientific_frame)
        frame4.pack(fill='x', padx=2, pady=2)
        for text in ['n!', '1/x', '|x|', 'e^x', 'Rand']:
            btn = ttk.Button(frame4, text=text, command=lambda t=text: self.on_scientific_click(t))
            btn.pack(side='left', expand=True, fill='x')

    def create_programming_buttons(self):
        # First row
        frame1 = ttk.Frame(self.programming_frame)
        frame1.pack(fill='x', padx=2, pady=2)
        for text in ['AND', 'OR', 'NOT', 'XOR', 'NAND']:
            btn = ttk.Button(frame1, text=text, command=lambda t=text: self.on_programming_click(t))
            btn.pack(side='left', expand=True, fill='x')
        
        # Second row
        frame2 = ttk.Frame(self.programming_frame)
        frame2.pack(fill='x', padx=2, pady=2)
        for text in ['<<', '>>', 'MOD', 'Bin', 'Hex']:
            btn = ttk.Button(frame2, text=text, command=lambda t=text: self.on_programming_click(t))
            btn.pack(side='left', expand=True, fill='x')
            
        # Third row
        frame3 = ttk.Frame(self.programming_frame)
        frame3.pack(fill='x', padx=2, pady=2)
        for text in ['Dec', 'Oct', '~', '&', '|']:
            btn = ttk.Button(frame3, text=text, command=lambda t=text: self.on_programming_click(t))
            btn.pack(side='left', expand=True, fill='x')

    def create_conversion_buttons(self):
        # Conversion types
        conversions = [
            "Length (m ↔ ft)",
            "Weight (kg ↔ lb)",
            "Temperature (°C ↔ °F)",
            "Area (m² ↔ ft²)",
            "Volume (L ↔ gal)"
        ]
        
        # Input field
        self.conv_input = ttk.Entry(self.conversion_frame, font=('Arial', 14))
        self.conv_input.pack(fill='x', padx=10, pady=10)
        
        # Result display
        self.conv_result = ttk.Label(self.conversion_frame, text="", font=('Arial', 14))
        self.conv_result.pack(fill='x', padx=10, pady=5)
        
        # Conversion buttons
        for conv in conversions:
            btn = ttk.Button(
                self.conversion_frame, 
                text=conv,
                command=lambda c=conv: self.perform_conversion(c)
            )
            btn.pack(fill='x', padx=5, pady=2)

    def on_button_click(self, text):
        if text == 'C':
            self.current_input = ""
        elif text == '⌫':
            self.current_input = self.current_input[:-1]
        elif text == '±':
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        elif text == '=':
            try:
                expr = self.current_input.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                self.current_input = str(result)
            except:
                self.current_input = "Error"
        elif text in ['MC', 'MR', 'MS', 'M+', 'M-']:
            self.handle_memory(text)
        else:
            self.current_input += text
            
        self.display_var.set(self.current_input)
        
    def on_scientific_click(self, text):
        try:
            if self.current_input == "Error":
                self.current_input = ""
                
            if text == 'sin':
                result = math.sin(math.radians(float(self.current_input)))
            elif text == 'cos':
                result = math.cos(math.radians(float(self.current_input)))
            elif text == 'tan':
                result = math.tan(math.radians(float(self.current_input)))
            elif text == 'asin':
                result = math.degrees(math.asin(float(self.current_input)))
            elif text == 'acos':
                result = math.degrees(math.acos(float(self.current_input)))
            elif text == 'atan':
                result = math.degrees(math.atan(float(self.current_input)))
            elif text == 'π':
                result = math.pi
                self.current_input = ""
            elif text == 'e':
                result = math.e
                self.current_input = ""
            elif text == 'log':
                result = math.log10(float(self.current_input))
            elif text == 'ln':
                result = math.log(float(self.current_input))
            elif text == '√':
                result = math.sqrt(float(self.current_input))
            elif text == 'x²':
                result = float(self.current_input) ** 2
            elif text == 'x³':
                result = float(self.current_input) ** 3
            elif text == 'x^y':
                self.current_input += '**'
                self.display_var.set(self.current_input)
                return
            elif text == '10^x':
                result = 10 ** float(self.current_input)
            elif text == 'n!':
                result = math.factorial(int(float(self.current_input)))
            elif text == '1/x':
                result = 1 / float(self.current_input)
            elif text == '|x|':
                result = abs(float(self.current_input))
            elif text == 'e^x':
                result = math.exp(float(self.current_input))
            elif text == 'Rand':
                result = np.random.random()
                
            self.current_input = str(result)
            self.display_var.set(self.current_input)
        except:
            self.current_input = "Error"
            self.display_var.set(self.current_input)
            
    def on_programming_click(self, text):
        try:
            if self.current_input == "Error":
                self.current_input = ""
                
            if text in ['Bin', 'Hex', 'Oct', 'Dec']:
                num = int(float(self.current_input))
                if text == 'Bin':
                    result = bin(num)
                elif text == 'Hex':
                    result = hex(num)
                elif text == 'Oct':
                    result = oct(num)
                else:  # Dec
                    result = str(num)
            elif text == 'AND':
                self.current_input += ' & '
                self.display_var.set(self.current_input)
                return
            elif text == 'OR':
                self.current_input += ' | '
                self.display_var.set(self.current_input)
                return
            elif text == 'NOT':
                result = ~int(float(self.current_input))
            elif text == 'XOR':
                self.current_input += ' ^ '
                self.display_var.set(self.current_input)
                return
            elif text == 'NAND':
                a = int(float(self.current_input))
                result = ~(a & a)
            elif text == '<<':
                self.current_input += ' << '
                self.display_var.set(self.current_input)
                return
            elif text == '>>':
                self.current_input += ' >> '
                self.display_var.set(self.current_input)
                return
            elif text == 'MOD':
                self.current_input += ' % '
                self.display_var.set(self.current_input)
                return
            elif text == '~':
                result = ~int(float(self.current_input))
            elif text == '&':
                self.current_input += ' & '
                self.display_var.set(self.current_input)
                return
            elif text == '|':
                self.current_input += ' | '
                self.display_var.set(self.current_input)
                return
                
            self.current_input = str(result)
            self.display_var.set(self.current_input)
        except:
            self.current_input = "Error"
            self.display_var.set(self.current_input)
            
    def perform_conversion(self, conversion_type):
        try:
            value = float(self.conv_input.get())
            if "Length" in conversion_type:
                if "m ↔ ft" in conversion_type:
                    result = value * 3.28084  # meters to feet
                    self.conv_result.config(text=f"{value} meters = {result:.2f} feet")
                else:
                    result = value / 3.28084  # feet to meters
                    self.conv_result.config(text=f"{value} feet = {result:.2f} meters")
            elif "Weight" in conversion_type:
                if "kg ↔ lb" in conversion_type:
                    result = value * 2.20462  # kg to lbs
                    self.conv_result.config(text=f"{value} kg = {result:.2f} pounds")
                else:
                    result = value / 2.20462  # lbs to kg
                    self.conv_result.config(text=f"{value} pounds = {result:.2f} kg")
            elif "Temperature" in conversion_type:
                if "°C ↔ °F" in conversion_type:
                    result = (value * 9/5) + 32  # C to F
                    self.conv_result.config(text=f"{value}°C = {result:.2f}°F")
                else:
                    result = (value - 32) * 5/9  # F to C
                    self.conv_result.config(text=f"{value}°F = {result:.2f}°C")
            elif "Area" in conversion_type:
                if "m² ↔ ft²" in conversion_type:
                    result = value * 10.7639  # m² to ft²
                    self.conv_result.config(text=f"{value} m² = {result:.2f} ft²")
                else:
                    result = value / 10.7639  # ft² to m²
                    self.conv_result.config(text=f"{value} ft² = {result:.2f} m²")
            elif "Volume" in conversion_type:
                if "L ↔ gal" in conversion_type:
                    result = value * 0.264172  # L to gal
                    self.conv_result.config(text=f"{value} liters = {result:.2f} gallons")
                else:
                    result = value / 0.264172  # gal to L
                    self.conv_result.config(text=f"{value} gallons = {result:.2f} liters")
        except:
            self.conv_result.config(text="Invalid input")

    def handle_memory(self, op):
        try:
            if op == 'MC':  # Memory Clear
                self.memory = 0
            elif op == 'MR':  # Memory Recall
                self.current_input += str(self.memory)
                self.display_var.set(self.current_input)
            elif op == 'MS':  # Memory Store
                self.memory = float(self.current_input)
            elif op == 'M+':  # Memory Add
                self.memory += float(self.current_input)
            elif op == 'M-':  # Memory Subtract
                self.memory -= float(self.current_input)
                
            self.memory_var.set(f"M: {self.memory}")
        except:
            self.current_input = "Error"
            self.display_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
