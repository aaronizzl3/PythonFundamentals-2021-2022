# Imports - these always go at the top
import datetime


# Data - anything that will be referred to in the program
films = ["The Batman", "Star Wars", "The Grinch", "Harry Potter", "James Bond"]

accounts = [
    ["ahussain", "password"],
    ["mlambert", "password12"]
]


# Functions
# Login - authorise any access to the application
def login():
    attempt = True
    while attempt:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for row in accounts:
            if username == row[0] and password == row[1]:
                attempt = False
                print("Access granted.\n")
                menu()
                break

                
# Allow the user to choose what to do, calling other functions
def menu():
    while True:
        option = int(input("MENU\n1 - Create Booking\n2 - View Previous Bookings\n3 - Exit\nOption: "))

        if option == 1:
            create_booking()
        elif option == 2:
            read_bookings()
        elif option == 3:
            print("Exiting.")
            break
        else:
            print("Invalid input. Try again.")


# Take inputs for creating a booking
def create_booking():
    print("The films available today would be:")
    for film in films:
        print(film)

    name = input("What name would you like the booking under? ")
    tickets = int(input("How many tickets would you like to buy? "))

    while True:
        film_choice = input("Which film would you like to see?")
        if film_choice in films:
            break
        else:
            print("That film isn't showing. Choose another.")

    save_booking(name, tickets, film_choice)


# Called from the create_booking, used specifically to save data
def save_booking(name, tickets, film_choice):
    try:
        date = datetime.date.today()
        myFile = open(f"{date}-{name}", "w")
        myFile.write(f"Name: {name} - Tickets: {tickets} - Film: {film_choice} - Showing Date: {date}")
        myFile.close()
        print("Booking created successfully!\n")
    except IOError as error:
        print(f"Unable to save booking. Error: {error}")


# Read a previous booking, based on date and name
def read_bookings():
    name = input("What name is the booking under? ")
    year = int(input("Year (2022): "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    date = datetime.date(year, month, day)

    try:
        myFile = open(f"{date}-{name}", "r")
        for line in myFile:
            print(line)
    except IOError as error:
        print(f"Error reading from file. Error: {error}")


# Main logic, call the login function to start the program
login()
