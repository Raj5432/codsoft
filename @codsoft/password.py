import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, include_name, name, include_number, number):
    if length < 4:
        raise ValueError("Length must be at least 4 for strength.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_chars = lower + upper + digits + punctuation

    password_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password_chars)
    password = ''.join(password_chars)

    if include_name and name:
        pos = secrets.randbelow(len(password) + 1)
        password = password[:pos] + name + password[pos:]

    if include_number and number:
        pos = secrets.randbelow(len(password) + 1)
        password = password[:pos] + number + password[pos:]

    return password

def generate_button_click():
    try:
        length = int(entry_length.get())
        include_name = include_name_var.get()
        name = entry_name.get() if include_name else ""
        include_number = include_number_var.get()
        number = entry_number.get() if include_number else ""

        password = generate_password(length, include_name, name, include_number, number)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        update_strength_label(password)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def update_strength_label(password):
    length = len(password)
    unique = len(set(password))

    if length >= 12 and unique > 8:
        strength = "Strong 🔒"
        color = "green"
    elif length >= 8:
        strength = "Moderate 🔑"
        color = "orange"
    else:
        strength = "Weak ⚠️"
        color = "red"

    strength_label.config(text=f"Strength: {strength}", fg=color)

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("✨ Unique Password Generator ✨")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#e0f7fa")  # light cyan

# Main frame
frame = tk.Frame(root, bg='white', bd=2, relief="ridge", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
label_title = tk.Label(frame, text="Secure Password Generator", font=("Helvetica", 18, "bold"), bg="white", fg="#333")
label_title.pack(pady=10)

# Password length
tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="white").pack()
entry_length = tk.Entry(frame, font=("Arial", 12))
entry_length.pack(pady=5)

# Include name
include_name_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Name", variable=include_name_var, bg="white").pack()
entry_name = tk.Entry(frame, font=("Arial", 12))
entry_name.pack(pady=5)

# Include number
include_number_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Include Number", variable=include_number_var, bg="white").pack()
entry_number = tk.Entry(frame, font=("Arial", 12))
entry_number.pack(pady=5)

# Generate button
generate_btn = tk.Button(frame, text="Generate Password", command=generate_button_click, bg="#007ACC", fg="white", font=("Arial", 12, "bold"))
generate_btn.pack(pady=10)

# Generated password
tk.Label(frame, text="Generated Password:", font=("Arial", 12), bg="white").pack()
entry_password = tk.Entry(frame, width=40, font=("Courier", 12), justify="center")
entry_password.pack(pady=5)

# Strength indicator
strength_label = tk.Label(frame, text="Strength:", font=("Arial", 12), bg="white")
strength_label.pack(pady=5)

# Copy button
copy_btn = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#28a745", fg="white", font=("Arial", 10))
copy_btn.pack(pady=5)

root.mainloop()
