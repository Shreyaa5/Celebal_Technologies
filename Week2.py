import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        return None

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")
        return None

# Function to update the display with the button click
def button_click(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to calculate the result
def calculate_result():
    expression = display_var.get()
    result = evaluate_expression(expression)
    if result is not None:
        display_var.set(str(result))
root = tk.Tk()
root.title("Simple Calculator")
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create the buttons and place them on the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=calculate_result)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

clear_btn = tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 18), command=clear_display)
clear_btn.grid(row=4, column=4)
root.mainloop()
