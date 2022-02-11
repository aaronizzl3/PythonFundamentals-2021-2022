"""
Research to find out how to generate random number between 1-3 in Python.
Create a game which gives the user a guess on what the random number is.
It should tell them whether they’re correct or not.
"""

import random

ourNumber = random.randint(1, 3)

myGuess = int(input("What is your guess?"))

if ourNumber == myGuess:
    print("Correct! You have won the game.")
else:
    print(f"Wrong! The correct number was {ourNumber}.")
