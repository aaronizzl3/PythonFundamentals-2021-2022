

# TODO: Upper and lower.
def Upper_Lower():
    myString = "hello, world!"
    print(myString.upper())
    print(myString.lower())


# TODO: Strip whitespace.
def Strip_Space():
    bigString = "      this string has space either side.       "
    print(bigString)
    print(bigString.strip())


# TODO: Replacing characters.
def Replace_Character():
    name = "aaron"
    for x in name:
        if x == "a":
            decrypt = name.replace("a", "b")

    print(decrypt)


# TODO: Splitting into substrings.
def Split_Strings():
    thisString = "These are words."
    newString = thisString.split(" ")
    print(newString)


Split_Strings()