
text = "Aaron Hussain"
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "defghijklmnopqrstuvwxyzabc"
result = ""

for letter in text:
    if letter.lower() in alphabet:
        result += key[alphabet.find(letter.lower())]
    else:
        result += letter

print(result)
