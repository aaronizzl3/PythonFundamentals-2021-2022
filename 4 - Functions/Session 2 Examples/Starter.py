
"""
Create an application that uses a list with the following numbers:

1, 7, 4, 2, 10, 8, 3

Using loops, the application should tell us how many numbers are larger than five,
and which specific numbers they are.

"""

my_numbers = [1, 7, 4, 2, 10, 8, 3]
counter = 0

for num in my_numbers:
    if num > 5:
        print(f"{num} is greater than five.")
        counter += 1

print(f"The total number over five was {counter}")


"""
Create a program that utilises a loop; allow the user to append five numbers of their choice to 
a list.

"""

my_list = []

for x in range(5):
    my_number = int(input("Enter a number: "))
    my_list.append(my_number)

print(my_list)
