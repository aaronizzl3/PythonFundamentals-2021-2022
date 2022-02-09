
# Generate a random number between 1-3, and have the user guess it

import random

generated_number = random.randint(1, 3)
option = int(input("What number do you think it is? "))

if generated_number == option:
    print("Correct!")
else:
    print("Wrong!")

print(f"Random Number: {generated_number}\nMy Number: {option}")
