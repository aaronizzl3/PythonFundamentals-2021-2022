"""

Create a function that takes a list as an argument and returns the first element.

Create a function that takes a number as an argument and returns True if it is less than or equal to zero.
Otherwise, return false.

"""


def first_element(food):
    return food[0]


def less_than_zero(number):
    if number <= 0:
        return True
    else:
        return False


# Printing the returns so that we can see their value in the console
print(first_element(["Spaghetti", "Carbonara", "Margherita", "Pepporoni"]))
print(less_than_zero(-4))
