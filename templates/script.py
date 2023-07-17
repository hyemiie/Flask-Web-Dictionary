from flask import Flask
import json
from difflib import get_close_matches


data= json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0 :
        yn = input("Did you mean %s instead? , Enter Y if yes and N if No:" % get_close_matches(word, data.keys())[0])
        if yn =='Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "Oops...this word doesn't exist"
        else:
            return "We don't understand your query"
    else:
        return "Oops...this word doesn't exist"


word = input('What definition are you looking for??: ')

answer = translate(word)

if type(answer) ==  list:
    for item in answer:
        print(item)
else :
    print(answer)

