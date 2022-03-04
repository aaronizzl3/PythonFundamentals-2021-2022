
# TODO: Take two parameters; favourite food, and how many times I eat it per week
# TODO: Return it in a string: "My favourite food is xxx and I eat it x times per week"

def form_sentence(food, frequency):
    sentence = f"My favourite food is {food} and I eat it {frequency} times per week"
    return sentence


myString = form_sentence("pizza", "7")
print(myString)

