
# FOR
print("What are your three favourite colours?")

for x in range(3):
    colour = input("")
    print(f"One of them is {colour}!")

# WHILE
y = 1

while y == 1:
    print("Hello World!")

    option = input("Do you want to continue?")
    if option == "Yes":
        continue
    else:
        y = 0

# FOR LOOP
for x in range(5):
    print("Hello World!")

    option = input("Do you want to continue?")
    if option == "Yes":
        continue
    elif option == "No":
        break

