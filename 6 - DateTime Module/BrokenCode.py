logged = False

# Username, Password, Access Level
accounts = [
    ["admin", "123", 1],
    ["user", "password", 0],
    ["ahuss", "collectstamps", 0],
    ["boss", "qwerty", 1],
    ["lemon123", "abcdefg", 0]
]

# Store logged in users details
loggedUser =

# Take inputs for the user to login to the system
username = "Enter your username: "
password = input("Enter your password: ")

# Search through the rows in the 2D lists, to find a matching username and password in the same row
for row in accounts:
    if row[0] == username and row[1] == password:
        print("Details correct - logged in!")
        logged = True

        # We require this section to create a single list, rather than a 2D list
        for column in row:
            loggedUser.append(column)
        break

# Menu system - this does not activate until the user is confirmed to have matching credentials
while logged:
    print(loggedUser)
    option = input('''Menu
    1 - Add User
    2 - Remove User
    3 - Exit Program
    Select Option: ''')

    # Respond to the input from the user, this option adds a new user to the row
    # CHALLENGE - this code is not efficient, try and improve it!
    if option == "1":
        addUser = True
        while addUser:
        userAdd = input("Enter username:")
        for row in accounts:
                if userAdd in accounts[0]:
                    print("User already exists, choose a new name...")
                else:
                    passAdd = input("Enter password: ")
                    authAdd = int(input("Enter auth level (1/0): "))
                    accounts.append([userAdd, passAdd, authAdd])
                    print(accounts)
                    addUser = False

    # This option will be used to remove a user - you will build this function by yourself once the rest is complete
    elif option == "2":
        # Pass is often used for empty blocks when testing code; this is a good placeholder
        pass

    # Exit program option
    elif option == "3":
        print("Exiting program...")
        logged = False

    # Catch all option - we can use the ELSE as a catch all for all other entries the user might attempt
    else
        print("Invalid input!")
