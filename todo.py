import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title(" My To-Do List 📝")
root.geometry("400x500")
root.config(bg="#1b505e")  

FILE_NAME = "tasks.txt"

tasks = []

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks Saved!")  

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())

def add_task():
  task = entry.get()

  if task != "":
   listbox.insert(tk.END, "" + task)
   entry.delete(0, tk.END)
  else:
     messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
 
    except:

     messagebox.showwarning("Warning", "Please select a task!")


def on_enter(e):
  e.widget.config(bg="#fafafa")

def on_closing():
    save_tasks()
    root.destroy()

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get().strip()

        if new_task:
            listbox.delete(selected)
            listbox.insert(selected, "" + new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter updated task!")
    
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def toggle_task_status():
    try:
        selected = listbox.curselection()[0]
        task_text = listbox.get(selected)

        if task_text.startswith("✔ "):
            
            updated_task = task_text.replace("✔ ", "")
        else:
            
            updated_task = "✔ " + task_text

        listbox.delete(selected)
        listbox.insert(selected, updated_task)

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to track!")



title = tk.Label(root, text=" MY TO-DO LIST 📝",
                font=("Arial", 20, "bold"),
                bg="#1b505e", fg="#000405")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=25)
entry.pack(pady=10)


button_frame = tk.Frame(root, bg="#1b505e")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", 
                font=("Arial", 9),
                bg="#31f50a",
                fg="black",
                command=add_task)
add_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(button_frame, text="Delete Task",
                   font=("Arial", 9),
                   bg="#f50a0a",
                   fg="black",
                   command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=10)


update_btn = tk.Button(button_frame, text="Update Task",
                   font=("Arial", 9),
                   bg="#0af5d9",
                   fg="black",
                   command=update_task)
update_btn.pack(side=tk.LEFT, padx=10)

track_btn = tk.Button(button_frame, text="✔ Track Task",
                   font=("Arial", 9),
                   bg="#b36bff",
                   fg="black",
                   command=toggle_task_status)
track_btn.pack(side=tk.LEFT, padx=10)


tk.Button(root, text="💾 Save Tasks",
          bg="#00c2ff",font=("Arial", 9),
          command=save_tasks).pack(pady=5)

listbox = tk.Listbox(root,
                 font=("Arial", 16),
                 width=30,
                 height=20)
listbox.pack(pady=15)

def load_selected_task(event):
    try:
        selected = listbox.curselection()[0]
        task_text = listbox.get(selected)
        entry.delete(0, tk.END)
        entry.insert(0, task_text.replace("", ""))
    except IndexError:
        pass

listbox.bind("<<ListboxSelect>>", load_selected_task)


def on_leave(e):
  e.widget.config(bg=e.widget.original_color)
for btn in [add_btn, delete_btn, update_btn,track_btn]:
   btn.original_color = btn["bg"]
   btn.bind("<Enter>", on_enter)
   btn.bind("<Leave>", on_leave)

load_tasks()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
