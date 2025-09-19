import tkinter as tk

# Function to update expression in the entry box
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())  # Not secure for real apps, but fine for beginners
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda val=text: button_click(val)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the application
root.mainloop()
