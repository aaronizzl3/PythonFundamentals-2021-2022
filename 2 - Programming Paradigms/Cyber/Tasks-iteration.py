

# A - Count up to ten with FOR

count = 0

for x in range(11):
    print(count)
    count += 1

# B - Count up to ten with WHILE

count = 0

while count < 11:
    print(count)
    count += 1


# C C – take an input for a number. Print out that number multiplied by 2,
# and repeat the print and multiplication four times.

myNumber = int(input("Enter a number: "))

for x in range(4):
    myNumber *= 2
    print(myNumber)


