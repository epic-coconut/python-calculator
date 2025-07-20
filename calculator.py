import tkinter as tk

def create_calculator():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")  # Window size

    # Display (Entry widget)
    display = tk.Entry(root, font=("Arial", 20), justify="right")
    display.pack(fill="x", padx=10, pady=10)

    # Button layout
    buttons = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("0", ".", "C", "+"),
        ("=",)
    ]

    # Function to handle button clicks
    def on_click(char):
        if char == "C":
            display.delete(0, tk.END)  # Clear display
        elif char == "=":
            try:
                result = eval(display.get())  # Calculate result
                display.delete(0, tk.END)
                display.insert(0, str(result))
            except:
                display.delete(0, tk.END)
                display.insert(0, "Error")
        else:
            display.insert(tk.END, char)  # Append button text

    # Create buttons
    for row in buttons:
        frame = tk.Frame(root)
        frame.pack(fill="x", padx=5, pady=5)
        for char in row:
            btn = tk.Button(frame, text=char, font=("Arial", 16), 
                          command=lambda c=char: on_click(c))
            btn.pack(side="left", expand=True, fill="x")

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
