# 1 - Read the file and append each line to a list, use a FUNCTION and RETURN if possible
def read_file():
    teams_list = []
    myFile = open("Teams.txt", "r")

    for line in myFile:
        teams_list.append(line.strip("\n"))

    return teams_list


# 2 - Add Newcastle to the list
def add_team(list):
    list.append("Newcastle")
    return list


# 3 - Print out the first element of the list
def print_first(list):
    print(list[0])


# 4 - Remove the team Sunderland from the list if it exists
def remove_sunderland(list):
    if "Sunderland" in list:
        list.remove("Sunderland")
    return list


my_list = read_file()
my_list = add_team(my_list)
print_first(my_list)
my_list = remove_sunderland(my_list)
print(my_list)
