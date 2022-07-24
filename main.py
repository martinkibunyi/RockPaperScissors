#Rock Paper Scissors Game
import random

user_wins  = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock, Paper or Scissors?\nQ to quit!!!\n").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_guess = options[random_number]
    print("Computer picked",computer_guess+".")

    if user_input == "paper" and computer_guess == "rock":
        print("You Won!!!")
        user_wins += 1

    elif user_input == "rock" and computer_guess == "scissors":
        print("You Won!!!")
        user_wins += 1

    elif user_input == "scissors" and computer_guess == "paper":
        print("You Won!!!")
        user_wins += 1

    elif user_input == "rock" and computer_guess == "rock":
        print("Try Again!!!")

    elif user_input == "paper" and computer_guess == "paper":
        print("Try Again!!!")

    elif user_input == "scissors" and computer_guess == "scissors":
        print("Try Again!!!")

    else:
        print("You Lost!!!")
        computer_wins += 1

print("You won",user_wins,"times!!!\nThe Computer won",computer_wins,"times!!!")
print("Goodbye!!!")
