import random

player = {
    "strength": 3
}

monster = {
    "strength": 7
}

option = input("Do you want to fight? Yes/No\nOption: ")

if option == "Yes":
    attack_roll = random.randint(1, 6)
    if player["strength"] + attack_roll > monster["strength"]:
        print("You have slain the beast!")
    else:
        print("Puny human, you have been smushed.")
else:
    print("You ran away.")