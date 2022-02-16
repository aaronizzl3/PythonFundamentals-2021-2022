"""
Write a program which has a list with four numbers.

Append a number to the end of the list.

Using an IF/ELSE, print out whether the first and last number in the last are equal or not.
"""

my_numbers = [7, 10, 3, 5]

my_numbers.append(7)

if my_numbers[0] == my_numbers[-1]:
    print("First and last are equal.")
else:
    print("First and last are NOT equal.")

print(sorted(my_numbers))