
text = "ddurq kxvvdlq"
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "defghijklmnopqrstuvwxyzabc"
result = ""

for letter in text:
    if letter.lower() in key:
        result += alphabet[key.find(letter.lower())]
    else:
        result += letter

print(result)
