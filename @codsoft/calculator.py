import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = variable_operation.get()
        
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Main frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=20)

# Title label
label_title = tk.Label(frame, text="Simple Calculator", font=("Arial", 20))
label_title.pack(pady=10)

# Number 1 entry
label_num1 = tk.Label(frame, text="Enter first number:", font=("Arial", 14))
label_num1.pack(pady=5)
entry_num1 = tk.Entry(frame, font=("Arial", 14))
entry_num1.pack(pady=5)

# Number 2 entry
label_num2 = tk.Label(frame, text="Enter second number:", font=("Arial", 14))
label_num2.pack(pady=5)
entry_num2 = tk.Entry(frame, font=("Arial", 14))
entry_num2.pack(pady=5)

# Operation choice
label_operation = tk.Label(frame, text="Choose operation:", font=("Arial", 14))
label_operation.pack(pady=5)
variable_operation = tk.StringVar(frame)
variable_operation.set("Add") # default value
operations = ["Add", "Subtract", "Multiply", "Divide"]
option_menu = tk.OptionMenu(frame, variable_operation, *operations)
option_menu.pack(pady=5)

# Calculate button
button_calculate = tk.Button(frame, text="Calculate", font=("Arial", 14), command=calculate)
button_calculate.pack(pady=20)

# Result label
label_result = tk.Label(frame, text="Result: ", font=("Arial", 14))
label_result.pack(pady=5)

root.mainloop()
