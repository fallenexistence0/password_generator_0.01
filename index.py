import secrets
import string
import csv
import hashlib

import tkinter as tk
from tkinter import messagebox

special_char = ['_','&','!','?',';','@','^']
special_char = ''.join(special_char)

def password_generator():
    include_special_char = special_var.get()
    password_length = int(length_entry.get())
    
    if include_special_char:
        allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_char
    else:
        allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase
        
    full_pass = ''.join(secrets.choice(allowed_char) for _ in range(password_length))

    # Print the generated password
    print("Generated Password:", full_pass)

    hashed_password = hash_password(full_pass)

    # Write both the password and hashed version to CSV
    with open('list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['password', 'hashed_password'])
        writer.writerow([full_pass, hashed_password])
    
    messagebox.showinfo("Password Generated", f"Hashed password: {hashed_password}")

def hash_password(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    return hasher.hexdigest()

# Create GUI window
root = tk.Tk()
root.title("Password Generator")

# GUI elements
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=password_generator)
generate_button.pack()

# Start GUI event loop
root.mainloop()
