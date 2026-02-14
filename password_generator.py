import tkinter as tk
import random
import string

# Generate Password
def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    result_label.config(text=password)

# Copy Password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.config(bg="#2c3e50")
# Title
tk.Label(root, text="Password Generator 🔐",
         font=("Arial", 20, "bold"),  bg="#2c3e50", fg="white").pack(pady=10)

# Length Input
tk.Label(root, text="Enter Password Length:",
          font=("Arial", 12, ),height=2,bg="#2c3e50", fg="white").pack()

length_entry = tk.Entry(root)
length_entry.insert(0, "8")
length_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate password 🗝",
          command=generate_password,font=("Arial", 10 ) ,width=20,height=0,
          bg="green", fg="white").pack(pady=10)

# Result
result_label = tk.Label(root, text="",
                        font=("Arial", 15),width=19,height=2)
result_label.pack(pady=10)

# Copy Button
tk.Button(root, text="Copy Password",
          command=copy_password,
          bg="#e67e22", fg="white").pack(pady=5)

root.mainloop()
