"""
Write a program which has a list; this list should have four numbers.

Using append, add an additional number to the end of the list.

Using an IF/ELSE statement, print if the first and last numbers
in the list are the same or not.

Extension
Try and test the functions listed on the right. Investigate how
they can be used to manipulate lists.
"""


# A
my_list = [10, 12, 7, 3]

# B
my_list.append(42)

# C
if my_list[0] == my_list[-1]:
    print("The first and last numbers are equal.")

# OR
if my_list[0] == my_list[len(my_list) - 1]:
    print("The first and last numbers are equal.")

# OR
if my_list[0] == my_list[4]:
    print("The first and last numbers are equal.")

# Sort the list
sorted_list = sorted(my_list)
print(f"Original: {my_list}\nSorted: {sorted_list}")