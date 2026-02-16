import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Rock Paper Scissors Game 🎮")
root.geometry("400x500")
root.config(bg="#2c3e50")

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
max_score = 5 

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0   Computer Score: 0")
    winner_label.config(text="")
    result_label.config(text="")

def play(user_choice):
    global user_score, computer_score
    
    if user_score == max_score or computer_score == max_score:
        return  

    computer_choice = random.choice(choices)
    result_label.config(text=f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        winner_label.config(text="It's a Tie! 🤝")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        winner_label.config(text="You Win! 🎉")
    else:
        computer_score += 1
        winner_label.config(text="Computer Wins! 😅")
    
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")

    if user_score == max_score:
        messagebox.showinfo("Game Over", "🎉 Congratulations! You Win the Game!")
    elif computer_score == max_score:
        messagebox.showinfo("Game Over", "😅 Computer Win the Game!")


title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=20)

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="🪨 Rock", width=10, font=("Arial", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="📄 Paper", width=10, font=("Arial", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="✂ Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2c3e50", fg="white")
result_label.pack(pady=10)

winner_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#f1c40f")
winner_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0   Computer Score: 0", font=("Arial", 12), bg="#2c3e50", fg="white")
score_label.pack(pady=20)

tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), command=reset_game).pack(pady=10)

root.mainloop()
