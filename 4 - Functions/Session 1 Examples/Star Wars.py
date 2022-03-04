"""
Luke Skywalker has a lot of family and friends. Help him remember what relation he is to everyone,
given a string.

Example:
Input – relation(“Darth Vader”)
Output – “Luke, I am your father.”

Darth Vader - Father
Leia - Sister
R2D2 - Droid
Kenobi - Tutor
"""


characters = {
    "Darth Vader": "Father",
    "Leia": "Sister",
    "R2D2": "Droid",
    "Kenobi": "Tutor"
}


def relation(name):
    print(f"Luke, I am your {characters[name]}!")


relation("Darth Vader")



