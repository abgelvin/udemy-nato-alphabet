student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Please enter a word: ").upper()

letters = [dictionary[letter] for letter in word]

print(letters)