student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

ask = True

def generate_phonetic():
    word = input("Please enter a word: ").upper()

    try:
        letters = [dictionary[letter] for letter in word]
    except KeyError:
        print('Sorry, only letter in the alphabet please.')
        generate_phonetic()
    else:
        print(letters)

generate_phonetic()