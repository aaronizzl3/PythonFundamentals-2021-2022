
weather = "Cold"
wallet = "Empty"

if weather == "Hot" and wallet == "Full":
    print("I am going to the shops, I am desperate for my cream egg.")
elif weather == "Hot" and wallet == "Empty":
    print("I will steal the cream egg.")
else:
    print("I'm not going to the shops.")

"""
Take an input from the user which allows them to say whether they are a student, 
a lecturer or a random.

Using an IF statement, print that they are authorised 
if they are a lecturer or a student.

If they are anything else, it should print that they are 
not authorised.

Extension
Can you create the program so that it sets all input to lowercase?
"""

role = input("Which role are you?")

if role.lower() == "lecturer" or role.lower() == "student":
    print("Access granted.")
else:
    print("Access denied.")




