

# TODO: Testing function.
def Reading_File():
    myFile = open("BrandNewFile.txt", "r")
    print(myFile.read())


# TODO: Append new lines or content to a file.
def Append_File():
    myFile = open("AppendFile.txt", "a")
    myFile.write("Python has injected some content.\n")
    myFile.close()


# TODO: Overwrite content.
def Write_File():
    myFile = open("AppendFile.txt", "w")
    myFile.write("HACKZOR2000 WAS HERE.")
    myFile.close()


# TODO: Creating a file.
def Create_File():
        myFile = open("SomeName.txt", "x")


# TODO: Write list to file.
def Write_List():
    myList = ["Apple", "Banana", "Pear"]
    myFile = open("BrandNewFile.txt", "a")

    for x in myList:
        myFile.write("\n")
        myFile.write(x)


# TODO: Function calls.
Write_List()
Reading_File()