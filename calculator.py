import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1] 
    equation.set(expression)

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.config(bg="#2c3e50")

expression = ""
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=('Arial', 30),
                 bd=10, insertwidth=2, width=13, borderwidth=4,
                 justify='right')
entry.grid(row=1, column=0, columnspan=4, pady=(5,15), padx=10)


title_label = tk.Label(root, text="Calculator 🧮",
                       font=('Arial', 20, 'bold'),
                       bg="#2c3e50",
                       fg="white")
title_label.grid(row=0, column=0, columnspan=4, pady=(10,5))


button_style = {
    "font": ('Arial', 14),
    "bd": 5,
    "width": 5,
    "height": 2,


}

buttons = [
    ('9', press), ('8', press), ('7', press), ('/', press),
    ('6', press), ('5', press), ('4', press), ('*', press),
    ('3', press), ('2', press), ('1', press), ('+', press),
    ('0', press), ('(', press), (')', press), ('-', press),
    ('.', press), ('C', clear), ('=', equal), ('⌫', backspace)
]

row = 2
col = 0

for (text, func) in buttons:
    
    if text == "=":
        bg_color = "green"
        fg_color = "white"
    elif text == "⌫":
        bg_color = "#e74c3c"
        fg_color = "white"
    else:
        bg_color = "white"
        fg_color = "black"

    tk.Button(root, text=text,
              command=lambda t=text, f=func: f(t) if f==press else f(),
              font=('Arial', 14),
              bd=5,
              width=5,
              height=2,
              bg=bg_color,
              fg=fg_color
              ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(7):
   root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
