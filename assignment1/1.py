import json
# saves the data to json file
def writing_file(data):
    with open("mydictionary.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

#tries to open json file, if error makes a new file
try:
   with open("mydictionary.json", "r", encoding="utf-8") as f:
        dictionary = json.load(f)
except OSError:
    dictionary = {"cat": "kissa", "dog": "koira"}
    writing_file(dictionary)

while True:
    #Hoping to get english word, can also be in any language as long as it is string
    translate = input("Enter the word to translate in English\nEmpty quits\n").lower().strip()

    if not translate:
        break

    if not translate.isalpha():
        print("Enter a English word!\n")
    elif translate in dictionary:
        print(dictionary[translate])
    else:
        definition = ""
        #Asking definition untill input is string.
        while True:
            definition = input("Word not found. Please input a definition: ").lower().strip()

            if not definition.isalpha():
                print("Enter the Finnish word")
            else:
                break

        dictionary[translate] = definition
        writing_file(dictionary)

    print("")


    




