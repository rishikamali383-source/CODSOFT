import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

def load_contacts_from_file():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except:
            return []

def save_contacts_to_file():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


root = tk.Tk()
root.title("Contact Book 📔")
root.geometry("750x600")
root.config(bg="#f0f2f5")

contacts = load_contacts_from_file()
filtered_contacts = contacts.copy()


def refresh_list():
    listbox.delete(0, tk.END)
    for contact in filtered_contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Error", "Name and Phone are required!")
        return

    if not phone.isdigit() or len(phone) < 10:
        messagebox.showwarning("Error", "Enter valid phone number!")
        return

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    save_contacts_to_file()
    search_contact()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")

def update_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a contact to update!")
        return

    index = selected[0]
    selected_contact = filtered_contacts[index]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Error", "Name and Phone required!")
        return

    if not phone.isdigit() or len(phone) < 10:
        messagebox.showwarning("Error", "Enter valid phone number!")
        return

    selected_contact.update({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts_to_file()
    search_contact()
    clear_fields()
    messagebox.showinfo("Updated", "Contact Updated Successfully!")

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Select a contact to delete!")
        return

    confirm = messagebox.askyesno("Confirm", "Are you sure?")
    if not confirm:
        return

    index = selected[0]
    selected_contact = filtered_contacts[index]
    contacts.remove(selected_contact)

    save_contacts_to_file()
    search_contact()
    clear_fields()
    messagebox.showinfo("Deleted", "Contact Deleted Successfully!")

def search_contact():
    global filtered_contacts
    keyword = search_entry.get().lower()

    if keyword == "":
        filtered_contacts = contacts.copy()
    else:
        filtered_contacts = [
            contact for contact in contacts
            if keyword in contact["name"].lower() or keyword in contact["phone"]
        ]

    refresh_list()

def show_details(event):
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    contact = filtered_contacts[index]

    clear_fields()
    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    address_entry.insert(0, contact["address"])


title = tk.Label(root, text="Contact Book 📔",
                 font=("Arial", 22, "bold"),
                 bg="#f0f2f5")
title.pack(pady=10)


search_frame = tk.Frame(root, bg="#f0f2f5")
search_frame.pack()

search_entry = tk.Entry(search_frame, width=40)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(search_frame, text="Search", bg="#4a7abc", fg="white",
          command=search_contact).grid(row=0, column=1)


list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=60, height=10,
                     yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)
listbox.bind("<<ListboxSelect>>", show_details)

scrollbar.config(command=listbox.yview)


entry_frame = tk.Frame(root, bg="#f0f2f5")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Name", bg="#f0f2f5").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(entry_frame, width=40)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(entry_frame, text="Phone", bg="#f0f2f5").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(entry_frame, width=40)
phone_entry.grid(row=1, column=1, pady=5)

tk.Label(entry_frame, text="Email", bg="#f0f2f5").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(entry_frame, width=40)
email_entry.grid(row=2, column=1, pady=5)

tk.Label(entry_frame, text="Address", bg="#f0f2f5").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(entry_frame, width=40)
address_entry.grid(row=3, column=1, pady=5)


btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", bg="#28a745", fg="white",
          width=12, command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", bg="#07b9ff",
          width=12, command=update_contact).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", bg="#dc3545", fg="white",
          width=12, command=delete_contact).grid(row=0, column=2, padx=5)


refresh_list()

root.mainloop()
