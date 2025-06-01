import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow for image handling

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
root.geometry("400x500")
root.resizable(False, False)  # Prevent resizing

# Load background image
bg_image = Image.open(r"C:\Users\yamala raju\Downloads\top-view-desk-concept-with-notepad.jpg")
bg_image = bg_image.resize((400, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Background label
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Main frame for calculator (with rounded corners look & padding)
frame = tk.Frame(root, padx=20, pady=20, bg='white', bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label
label_title = tk.Label(frame, text="Simple Calculator", font=("Helvetica", 18, "bold"), bg='white', fg="#333")
label_title.pack(pady=10)

# First number entry
label_num1 = tk.Label(frame, text="Enter first number:", font=("Helvetica", 12), bg='white')
label_num1.pack(pady=2)
entry_num1 = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief="groove")
entry_num1.pack(pady=5)

# Second number entry
label_num2 = tk.Label(frame, text="Enter second number:", font=("Helvetica", 12), bg='white')
label_num2.pack(pady=2)
entry_num2 = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief="groove")
entry_num2.pack(pady=5)

# Operation selection
label_operation = tk.Label(frame, text="Choose operation:", font=("Helvetica", 12), bg='white')
label_operation.pack(pady=2)
variable_operation = tk.StringVar(frame)
variable_operation.set("Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
option_menu = tk.OptionMenu(frame, variable_operation, *operations)
option_menu.config(font=("Helvetica", 11))
option_menu.pack(pady=5)

# Calculate button
button_calculate = tk.Button(frame, text="Calculate", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=calculate)
button_calculate.pack(pady=10, ipadx=10, ipady=3)

# Result label
label_result = tk.Label(frame, text="Result: ", font=("Helvetica", 12, "bold"), bg='white', fg="#000")
label_result.pack(pady=5)

root.mainloop()
