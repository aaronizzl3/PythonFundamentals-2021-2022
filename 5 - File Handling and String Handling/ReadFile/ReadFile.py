

# TODO: Read() a file.
def Reading():
    myFile = open("ReadFile.txt", "r")
    test = myFile.read()
    print(test)


# TODO: Readline() one at a time.
def Reading_Lines():
    myFile = open("ReadFile.txt", "r")
    print(myFile.readlines())


# TODO: Loop through each line of a file.
def Reading_Loop():
    myFile = open("ReadFile.txt", "r")
    for line in myFile:
        print(line)


# TODO: Read the contents of a file into a string.
def Reading_String():
    myString = open('Readfile.txt', "r").read().replace("\n", " ")
    print(myString)


# TODO: Function calls (for ease).
Reading()