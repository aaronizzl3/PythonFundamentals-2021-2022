text = "ddurq kxvvdlq"
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
shift = 0

for i in range(26):
    for letter in text:
        if letter.lower() in alphabet:
            result += alphabet[alphabet.find(letter.lower()) - shift]
        else:
            result += letter
    print(result)
    result = ""
    shift += 1