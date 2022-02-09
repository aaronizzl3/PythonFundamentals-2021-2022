
# FOR LOOP - we know how many times our code will repeat

for x in range(5):
    print(f"Iteration {x}: Hello World!")

# RANDOM TASK
import random

randomNumber = random.randint(1,3)

for x in range(3):
    myGuess = int(input("Guess the random number: "))

    if myGuess == randomNumber:
        print("You have guessed correctly!")
        break
    else:
        print("Incorrect guess!")
