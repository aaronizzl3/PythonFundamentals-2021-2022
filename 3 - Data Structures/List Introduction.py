
# LISTS

my_names = ["John", "Jacob", "Jingleheimer", "Schmidt"]

print(my_names[1])

my_student = ["Aaron Hussain", 28, "Cyber Security and Networking"]
print(my_student)
print(my_student[2])

# Accessing Values
my_student[1] += 1
print(my_student)

# Add and Remove
my_student.append("First Year")
print(my_student)

my_student.remove("First Year")
print(my_student)

my_student.pop(0)
print(my_student)

# Iteration
my_fruits = ["Apple", "Pear", "Plum"]
for item in my_fruits:
    print(f"I love {item}")

my_numbers = [1, 2, 3]
for x in my_numbers:
    print(x + 1)


