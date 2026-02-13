import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title(" My To-Do List 📝")
root.geometry("400x500")
root.config(bg="#1b505e")  

tasks = []

def add_task():
  task = entry.get()

  if task != "":
   listbox.insert(tk.END, "✨ " + task)
   entry.delete(0, tk.END)
  else:
     messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
 
    except:

     messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    listbox.delete(0, tk.END)

def on_enter(e):
  e.widget.config(bg="#fafafa")


title = tk.Label(root, text=" MY TO-DO LIST 📝",
                font=("Arial", 20, "bold"),
                bg="#1b505e", fg="#000405")
title.pack(pady=10)


entry = tk.Entry(root, font=("Arial", 20), width=25)
entry.pack(pady=10)


button_frame = tk.Frame(root, bg="#1b505e")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", 
                font=("Arial", 12),
                bg="#31f50a",
                fg="black",
                command=add_task)
add_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(button_frame, text="Delete Task",
                   font=("Arial", 12),
                   bg="#f50a0a",
                   fg="black",
                   command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(button_frame, text="Clear All",
                  font=("Arial", 12),
                  bg="#f5a60a",
                  fg="black",
                  command=clear_tasks)
clear_btn.pack(side=tk.LEFT, padx=10)


listbox = tk.Listbox(root,
                 font=("Arial", 16),
                 width=30,
                 height=20)
listbox.pack(pady=15)


def on_leave(e):
  e.widget.config(bg=e.widget.original_color)
for btn in [add_btn, delete_btn, clear_btn]:
   btn.original_color = btn["bg"]
   btn.bind("<Enter>", on_enter)
   btn.bind("<Leave>", on_leave)

root.mainloop()  
