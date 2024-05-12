import tkinter as tk
import random
from PIL import Image, ImageTk

user_score = 0
comp_score = 0

def gen_comp_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def draw_game():
    global user_score, comp_score
    msg.config(text="Game was Draw. Play again.", bg="#081b31")
    
def show_winner(user_win, user_choice, comp_choice):
    global user_score, comp_score
    if user_win:
        user_score += 1
        user_score_para.config(text=user_score)
        msg.config(text=f"You win! Your {user_choice} beats {comp_choice}", bg="green")
    else:
        comp_score += 1
        comp_score_para.config(text=comp_score)
        msg.config(text=f"You lost. {comp_choice} beats your {user_choice}", bg="red")

def play_game(user_choice):
    comp_choice = gen_comp_choice()
    if user_choice == comp_choice:
        draw_game()
    else:
        user_win = True
        if user_choice == "rock":
            user_win = comp_choice == "paper" 
        elif user_choice == "paper":
            user_win = comp_choice == "scissors"
        else:
            user_win = comp_choice == "rock"
        show_winner(user_win, user_choice, comp_choice)

def on_choice_click(user_choice):
    play_game(user_choice)

root = tk.Tk()
root.title("Rock Paper Scissors")

# Heading
heading = tk.Label(root, text="Welcome to Rock Paper Scissors Game: ", font=("Algerian", 30), pady=100)
heading.pack()

choices_frame = tk.Frame(root)
choices_frame.pack(expand=True)

rock_img = ImageTk.PhotoImage(Image.open(r"C:\Users\HP\Downloads\Rock Paper Scissor\rock.png").resize((250, 250)))
rock_choice = tk.Button(choices_frame, command=lambda: on_choice_click("rock"), image=rock_img)
rock_choice.pack(side=tk.LEFT, padx=10, pady=10)

paper_img = ImageTk.PhotoImage(Image.open(r"C:\Users\HP\Downloads\Rock Paper Scissor\paper.png").resize((250, 250)))
paper_choice = tk.Button(choices_frame, command=lambda: on_choice_click("paper"), image=paper_img)
paper_choice.pack(side=tk.LEFT, padx=10, pady=10)

scissors_img = ImageTk.PhotoImage(Image.open(r"C:\Users\HP\Downloads\Rock Paper Scissor\scissors.png").resize((250, 250)))
scissors_choice = tk.Button(choices_frame, command=lambda: on_choice_click("scissors"), image=scissors_img)
scissors_choice.pack(side=tk.LEFT, padx=10, pady=10)

score_frame = tk.Frame(root)
score_frame.pack(expand=True)

user_score_label = tk.Label(score_frame, text="You", font=("Algerian", 14))
user_score_label.pack(side=tk.LEFT, padx=10, pady=10)

user_score_para = tk.Label(score_frame, text=user_score, font=("Algerian", 18))
user_score_para.pack(side=tk.LEFT, padx=10, pady=10)

comp_score_label = tk.Label(score_frame, text="Comp", font=("Algerian", 14))
comp_score_label.pack(side=tk.LEFT, padx=10, pady=10)

comp_score_para = tk.Label(score_frame, text=comp_score, font=("Algerian", 18))
comp_score_para.pack(side=tk.LEFT, padx=10, pady=10)

msg = tk.Label(root, text="Play your move", bg="#081b31", fg="white", font=("Algerian", 12), pady=10)
msg.pack(fill=tk.BOTH, expand=True)

root.mainloop()
