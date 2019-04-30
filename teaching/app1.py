import json
from difflib import get_close_matches

# Load JSON file with dictionary data
data = json.load(open("data.json"))


def translate(w):
    # Convert all user input to lowercase letters
    w = w.lower()

    # See if input matches JSON dictionary
    if w in data:
        return data[w]
    # Capitalize first letter and check for matches in dictionary file
    elif w.title() in data:
        return data[w.title()]

    # Apply uppercase to all letters and check for matches in dictionary file
    elif w.upper() in data:
        return data[w.upper()]

    # Suggestions if there aren't any matches and confirm correct input
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't get your entry."
    else:
        return "The word doesn't exist please double check it."


def initiate():
    anotherWord = ""
    while anotherWord == "":
        word = input("Enter word: ")
        output = translate(word)
        i = 1

        if type(output) == list:
            for item in output:
                print(i, item)
                i += 1
        else:
            print(output)

        anotherWord = input("Hit Enter to query another word...")
    if anotherWord != "":
        print("See you next time")


initiate()
