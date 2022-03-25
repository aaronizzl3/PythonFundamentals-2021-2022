"""
A rock paper scissors game, with user input and a randomly generated choice for the computer.
"""

# imports
import random

# logic
user_choice = input("Rock, Paper or Scissors? (R/P/S)")
computer_choice = random.randint(1, 3)

if user_choice == "R":
    if computer_choice == 1:
        print("Draw! The opponent chose rock too.")
    elif computer_choice == 2:
        print("You lose! The opponent covers your rock.")
    else:
        print("Victory! You crush the scissors.")
elif user_choice == "P":
    if computer_choice == 1:
        print("Victory! You cover the opponents rock.")
    elif computer_choice == 2:
        print("Draw! Paper on paper!")
    else:
        print("You lose! The scissors cut you apart.")
elif user_choice == "S":
    if computer_choice == 1:
        print("You lose! The rock smashes your scissors.")
    elif computer_choice == 2:
        print("You win! You slice up that paper to bits with your scissors.")
    else:
        print("Scissors on scissors? A draw!")
