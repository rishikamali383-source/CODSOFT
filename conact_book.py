import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Contact Book 📔")
root.geometry("550x600")
root.config(bg="#2c3e50")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def load_contacts():
    listbox.delete(0, tk.END)
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split("|")
                listbox.insert(tk.END, f"{name} - {phone}")
    except FileNotFoundError:
        pass

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        with open("contacts.txt", "a") as file:
            file.write(f"{name}|{phone}|{email}|{address}\n")

        messagebox.showinfo("Success", "Contact Added Successfully!")
        clear_fields()
        load_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    with open("contacts.txt", "r") as file:
        lines = file.readlines()

    lines.pop(index)

    with open("contacts.txt", "w") as file:
        file.writelines(lines)

    messagebox.showinfo("Deleted", "Contact Deleted Successfully!")
    load_contacts()

def search_contact():
    search = search_entry.get().lower()
    listbox.delete(0, tk.END)

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split("|")
                if search in name.lower() or search in phone:
                    listbox.insert(tk.END, f"{name} - {phone}")
    except FileNotFoundError:
        pass

def show_details(event):
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    with open("contacts.txt", "r") as file:
        lines = file.readlines()

    name, phone, email, address = lines[index].strip().split("|")

    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, phone)

    email_entry.delete(0, tk.END)
    email_entry.insert(0, email)

    address_entry.delete(0, tk.END)
    address_entry.insert(0, address)


title = tk.Label(root, text="Contact Book 📔", font=("Arial", 20, "bold"),
                 bg="#2c3e50", fg="white")
title.pack(pady=15)

tk.Label(root, text="Name", bg="#2c3e50", fg="white").pack()
name_entry = tk.Entry(root, width=45 )
name_entry.pack(pady=5)

tk.Label(root, text="Phone", bg="#2c3e50", fg="white").pack()
phone_entry = tk.Entry(root, width=45)
phone_entry.pack(pady=5)

tk.Label(root, text="Email", bg="#2c3e50", fg="white").pack()
email_entry = tk.Entry(root, width=45)
email_entry.pack(pady=5)

tk.Label(root, text="Address", bg="#2c3e50", fg="white").pack()
address_entry = tk.Entry(root, width=45)
address_entry.pack(pady=5)

tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=20, command=delete_contact).pack(pady=5)

tk.Label(root, text="Search Contact", bg="#2c3e50", fg="white").pack(pady=5)
search_entry = tk.Entry(root, width=45)
search_entry.pack(pady=5)
tk.Button(root, text="Search", width=20, command=search_contact).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=15)
listbox.bind("<<ListboxSelect>>", show_details)


load_contacts()

root.mainloop()
