# Create two variables which hold the values 4 & 7.
# Create an IF statement to prove which one is larger than the other.

numberA = 4
numberB = 7

if numberA > numberB:
    print("A > B")
elif numberA == numberB:
    print("A == B")
else:
    print("B > A")

# Store the name “Student”. Create an IF statement
# which shows they’re an admin, student or unauthorised.

role = "Student"

if role == "Student":
    print("This is a student account.")
elif role == "Admin":
    print("This is an admin account.")
else:
    print("This is account is unauthorised.")

# Create an IF statement that checks if a user likes
# apples and is older than twenty one.

LikesApples = True
MyAge = 28

if LikesApples and MyAge > 21:
    print("I like apples and I'm older than 21.")
else:
    print("I do not like apples, or perhaps I'm younger than 21.")
