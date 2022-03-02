
"""
Create an application that uses a list with the following numbers:

1, 7, 4, 2, 10, 8, 3

Loop through the list and tell us:
1. Which numbers are larger than five
2. How many numbers are larger than five.
"""

myList = [1, 7, 4, 2, 10, 8, 3]
count = 0

for number in myList:
    if number > 5:
        print(f"{number} is greater than five.")
        count += 1

print(f"The total number of values greater than five is {count}.")
