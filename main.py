import pandas
alphabet = (pandas.read_csv("nato_phonetic_alphabet.csv"))

new_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}

word_input = input("Write a word: ").upper()

answer_words = [new_alphabet[letter] for letter in word_input]

print(answer_words)
