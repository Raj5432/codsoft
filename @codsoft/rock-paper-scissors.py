import tkinter as tk
from tkinter import messagebox
import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Initialize scores and rounds
user_score = 0
computer_score = 0
rounds = 0
max_rounds = 5  # Set the number of rounds for the game

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def play_game(user_choice):
    global rounds
    if rounds < max_rounds:
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        rounds += 1
        if rounds == max_rounds:
            display_final_result()

def display_result(user_choice, computer_choice, result):
    result_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    result_message += f"\n\nScores - You: {user_score}, Computer: {computer_score}\nRounds: {rounds}/{max_rounds}"
    result_label.config(text=result_message)

def display_final_result():
    if user_score > computer_score:
        final_result = "Congratulations! You won the game!"
    elif user_score < computer_score:
        final_result = "Sorry! The computer won the game."
    else:
        final_result = "It's a tie game!"
    messagebox.showinfo("Final Result", final_result)
    reset_game()

def reset_game():
    global user_score, computer_score, rounds
    user_score = 0
    computer_score = 0
    rounds = 0
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Main frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=20)

# Title label
label_title = tk.Label(frame, text="Rock, Paper, Scissors", font=("Arial", 20))
label_title.pack(pady=10)

# Instructions label
label_instructions = tk.Label(frame, text="Choose rock, paper, or scissors:", font=("Arial", 14))
label_instructions.pack(pady=10)

# Buttons for choices
button_rock = tk.Button(frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play_game("rock"))
button_rock.pack(side=tk.LEFT, padx=5)

button_paper = tk.Button(frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play_game("paper"))
button_paper.pack(side=tk.LEFT, padx=5)

button_scissors = tk.Button(frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play_game("scissors"))
button_scissors.pack(side=tk.LEFT, padx=5)

# Result label
result_label = tk.Label(frame, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
