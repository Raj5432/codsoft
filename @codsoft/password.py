import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, include_name, name, include_number, number):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + punctuation

    # Generate a password of the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Add name and number if included
    if include_name:
        password += name
    if include_number:
        password += number

    return password

def generate_button_click():
    try:
        # Get the desired password length from the entry widget
        length = int(entry_length.get())

        # Get the name and number options
        include_name = include_name_var.get()
        name = entry_name.get() if include_name else ""
        
        include_number = include_number_var.get()
        number = entry_number.get() if include_number else ""

        if length <= 0:
            messagebox.showerror("Error", "Password length should be a positive integer.")
        else:
            # Generate and display the password
            password = generate_password(length, include_name, name, include_number, number)
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Main frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=20)

# Length input
label_length = tk.Label(frame, text="Enter the desired password length:")
label_length.pack(pady=10)
entry_length = tk.Entry(frame)
entry_length.pack(pady=5)

# Name inclusion
include_name_var = tk.BooleanVar()
check_name = tk.Checkbutton(frame, text="Include Name", variable=include_name_var)
check_name.pack(pady=5)
entry_name = tk.Entry(frame)
entry_name.pack(pady=5)

# Number inclusion
include_number_var = tk.BooleanVar()
check_number = tk.Checkbutton(frame, text="Include Number", variable=include_number_var)
check_number.pack(pady=5)
entry_number = tk.Entry(frame)
entry_number.pack(pady=5)

# Generate button
button_generate = tk.Button(frame, text="Generate Password", command=generate_button_click)
button_generate.pack(pady=10)

# Result label
label_password = tk.Label(frame, text="Generated Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(frame, width=40)
entry_password.pack(pady=5)

# Start the main loop
root.mainloop()
