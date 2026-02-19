import tkinter as tk
import random
import time

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
max_score = 5 

def play(user_choice):
    global user_score, computer_score
    
    
    options = ["✊", "🖐", "✌"]
    computer_choice = random.choice(options)
    
    user_move_display.config(text=f"{user_choice}")
    computer_move_display.config(text=f"{computer_choice}")
    
    if user_choice == computer_choice:
        result = "DRAW!"
        color = "gray"
    elif (user_choice == "✊" and computer_choice == "✌") or \
         (user_choice == "🖐" and computer_choice == "✊") or \
         (user_choice == "✌" and computer_choice == "🖐"):
        result = "YOU WIN! 🎉"
        user_score += 1
        color = "#28a745" 
    else:
        result = "PC WINS! 🙂"
        computer_score += 1
        color = "#dc3545" 
        
    winner_label.config(text=result, fg=color)
    score_label.config(text=f"YOU: {user_score}   |   PC: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    user_move_display.config(text="?")
    computer_move_display.config(text="?")
    winner_label.config(text="READY?", fg="black")
    score_label.config(text="YOU: 0   |   PC: 0")

root = tk.Tk()
root.title("rock paper scissors")
root.geometry("500x500")
root.configure(bg="#1e1e1e") 

tk.Label(root, text="rock paper scissors 🎮", font=("Impact", 28), bg="#1e1e1e", fg="white").pack(pady=20)


winner_frame = tk.Frame(root, bg="#1e1e1e")
winner_frame.pack(pady=20, fill="x")

user_box = tk.Frame(winner_frame, bg="#333", width=150, height=150)
user_box.pack_propagate(False)
user_box.pack(side="left", padx=40)
tk.Label(user_box, text="PLAYER", bg="#333", fg="#00d2ff").pack()
user_move_display = tk.Label(user_box, text="?", font=("Arial", 30, "bold"), bg="#333", fg="white")
user_move_display.pack(expand=True)


tk.Label(winner_frame, text="VS", font=("Impact", 24), bg="#1e1e1e", fg="#298D0B").pack(side="left")

pc_box = tk.Frame(winner_frame, bg="#333", width=150, height=150)
pc_box.pack_propagate(False)
pc_box.pack(side="right", padx=40)
tk.Label(pc_box, text="COMPUTER", bg="#333", fg="#ff4b2b").pack()
computer_move_display = tk.Label(pc_box, text="?", font=("Arial", 30, "bold"), bg="#333", fg="white")
computer_move_display.pack(expand=True)


winner_label = tk.Label(root, text="CHOOSE YOUR WEAPON", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
winner_label.pack(pady=10)

score_label = tk.Label(root, text="YOU: 0   |   PC: 0", font=("Courier", 14), bg="#1e1e1e", fg="#aaa")
score_label.pack(pady=5)


btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

moves = [("✊ Rock", "✊"), ("🖐 Paper", "🖐"), ("✌ Scissors", "✌")]
for text, choice in moves:
    tk.Button(btn_frame, text=text, width=10, bg="#444", fg="white", font=("Arial", 10, "bold"),
              command=lambda c=choice: play(c)).grid(row=0, column=moves.index((text,choice)), padx=5)

tk.Button(root, text="RESET", command=reset_game, bg="#222", fg="white").pack(pady=10)

root.mainloop()
