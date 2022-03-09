"""
MAIN TASKS
Create functions to:
Create a file named “Hockey.txt”
Append “Anaheim”, “Dallas” and “Chicago” to the file
Write “Mighty Ducks” to the file
"""


def create_hockey():
    my_file = open("Hockey.txt", "x")


def append_teams():
    my_file = open("Hockey.txt", "a")
    teams = ["Anaheim", "Dallas", "Chicago"]
    for team in teams:
        my_file.write(team)
    my_file.close()


def write_mighty_ducks():
    my_file = open("Hockey.txt", "w")
    my_file.write("Mighty Ducks")
    my_file.close()


"""
CHALLENGE
Create a file which stores some usernames inside. Read them into a list.
The user should be able to add a new username to the list, which should then save back to the file.
"""


# 1 - Open a file, read them into a list
def get_usernames():
    usernames = []
    my_file = open("Usernames.txt", "r")
    for name in my_file:
        usernames.append(name.strip("\n"))
    return usernames


# 2 - Add a new username to the list from user input
def add_username(data):
    new_username = input("Enter username to add: ")
    data.append(new_username)
    return data


# 3 - Write the list of usernames back to the file
def write_file(data):
    my_file = open("Usernames.txt", "w")
    for name in data:
        my_file.write(f"{name}\n")
    my_file.close()


my_list = get_usernames()
updated_list = add_username(my_list)
write_file(updated_list)