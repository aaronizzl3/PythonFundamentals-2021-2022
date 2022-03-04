
# 1 - Two numbers, subtract
def subtraction():
    numA = 5
    numB = 3
    answer = numA - numB
    print(answer)


# 2 - Take two numbers as parameters, multiply
def multiplication(numA, numB):
    answer = numA * numB
    print(answer)


# 3 - Take two parameters for firstname and surname, return
def form_name(forename, surname):
    full_name = f"{forename} {surname}"
    return full_name


# Function Calls
subtraction()
multiplication(10, 5)
my_value = form_name("Aaron", "Hussain")
print(f"My name is {my_value}")

