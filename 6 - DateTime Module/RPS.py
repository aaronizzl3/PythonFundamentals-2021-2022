
import random

# Us
option = int(input("1 - Scissors\n2 - Rock\n3 - Paper\nOption: "))

# Opponent
ranNumber = random.randint(1,3)

if ranNumber == 1:
    print("Scissors")
elif ranNumber == 2:
    print("Rock")
else:
    print("Paper")

if option == ranNumber:
    print("It's a draw")
elif option == 1 and ranNumber == 2:
