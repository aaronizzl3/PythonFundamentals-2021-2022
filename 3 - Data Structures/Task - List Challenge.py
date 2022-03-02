
# Create List
my_numbers = [4, 10, 12, 1, 4, 5, 9, 10, 11]

# Counters
even_counter = 0
odd_counter = 0

# Loop through List
for x in my_numbers:
    if x % 2 == 0:
        print(f"{x} is even.")
        even_counter += 1
    else:
        print(f"{x} is odd.")
        odd_counter += 1

print(f"Odd numbers: {odd_counter}\nEven Numbers: {even_counter}")
