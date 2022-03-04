
# Largest and Smallest - you can use min() and max()
def find_largest_smallest(data):
    largest = data[0]
    smallest = data[0]

    for x in data:
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x

    print(f"Smallest: {smallest}\nLargest: {largest}\nList: {data}\n")


find_largest_smallest([4,10,7,5,3,13,8,2])


# Sum numbers in a list - you can use sum()
def sum_list(data):
    total = 0

    for x in data:
        total += x

    print(f"Sum: {total}\nList: {data}\n")


sum_list([4,10,7,5,3,13,8,2])


# Reverse String - you can use reverse()
def reverse_string(data):
    new_string = ""
    string_length = len(data)
    counter = string_length

    for x in range(string_length):
        new_string += data[counter - 1]
        counter -= 1

    print(f"Reversed String: {new_string}\nOriginal: {data}\n")


reverse_string("blast")


# In Range
def in_range(min, max, number):
    if min <= number <= max:
        print(f"{number} is in range of {min} - {max}.\n")
    else:
        print(f"{number} is not in the range of {min} - {max}.\n")


in_range(1, 10, 15)
