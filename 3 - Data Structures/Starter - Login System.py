
"""
Create a system which takes a username and password.
INPUT

If the username and password matches "admin" and "password", allow access.
IF/ELSE

The user should be allowed three attempts.
FOR/WHILE

EXTENSION - Open a menu which allows the user to find today's date, or exit.
"""

import datetime

access = False

# LOGIN SYSTEM
for x in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "password":
        print("Access granted.")
        access = True
        break
    else:
        print("Access DENIED.")

# MENU SYSTEM
while access:
    option = int(input("1 - Today's Date\n2 - Exit\nOption: "))

    if option == 1:
        print(f"Today's date is {datetime.date.today()}")
    elif option == 2:
        print("Exiting program.")
        break
    else:
        print("Invalid input.")




