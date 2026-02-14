import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("My To-Do List 📝")
root.geometry("400x520")
root.config(bg="#1b505e")

FILE_NAME = "tasks.txt"

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks Saved!")   # check terminal


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())


def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, "➡ " + task)
        entry.delete(0, tk.END)
        save_tasks()   # auto save
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def clear_tasks():
    listbox.delete(0, tk.END)
    save_tasks()

def on_closing():
    save_tasks()
    root.destroy()

tk.Label(root, text="MY TO-DO LIST 📝",
         font=("Arial", 20, "bold"),
         bg="#1b505e", fg="black").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18), width=25)
entry.pack(pady=10)

frame = tk.Frame(root, bg="#1b505e")
frame.pack(pady=10)

tk.Button(frame, text="Add Task", bg="#31f50a",
          command=add_task).pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Delete Task", bg="#f50a0a",
          command=delete_task).pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Clear All", bg="#f5a60a",
          command=clear_tasks).pack(side=tk.LEFT, padx=5)

tk.Button(root, text="💾 Save Tasks",
          bg="#00c2ff",
          command=save_tasks).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 16),
                     width=30, height=15)
listbox.pack(pady=10)

relief="flat"


load_tasks()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

