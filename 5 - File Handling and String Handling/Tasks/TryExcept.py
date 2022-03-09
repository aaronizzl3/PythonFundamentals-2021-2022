
try:
    myFile = open("hello.txt", "r")
    print("File opened successfully.")
except IOError as error:
    print(f"Error: {error}")


