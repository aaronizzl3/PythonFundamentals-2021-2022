
"""
Create a login system with three attempts to login.
Upon successful login, print a menu to give the date or exit.
"""

import datetime


menu = False

# LOGIN SCRIPT
for x in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "password":
        print("Authorised.")
        menu = True
        break
    else:
        print("Unauthorised. Try again.")

# MENU SCRIPT
while menu:
    option = int(input("1 - Today's Date\n2 - Exit\nOption: "))

    if option == 1:
        print(f"Today's date is {datetime.date.today()}")
    elif option == 2:
        print("Exiting.")
        break
    else:
        print("Invalid input.")


