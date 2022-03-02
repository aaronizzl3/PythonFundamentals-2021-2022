"""
Create a function which when called, subtracts one number from another.

Create a function which takes two numbers as arguments. It should multiply them together and print the answer.

Create a function that asks the user to input their name. This should be returned so that it can be printed outside
the function.
"""


# 1
def subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a} - {b} = {a - b}")


# 2
def multiplication(x, y):
    print(x * y)


# 3
def enter_name():
    name = input("Enter your name: ")
    return name


myName = enter_name()
print("My name is " + myName)

