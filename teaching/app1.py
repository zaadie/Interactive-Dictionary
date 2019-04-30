import json


data = json.open("data.json")

def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist please double check it."


word = input("Enter word:")

print(translate(word))