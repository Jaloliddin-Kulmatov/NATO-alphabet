import pandas

alphabet = (pandas.read_csv("nato_phonetic_alphabet.csv"))

new_alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}
def generate_nato_alphabet():
    word_input = input("Write a word: ").upper()
    try:
        answer_words = [new_alphabet[letter] for letter in word_input]
    except KeyError:
        print("Sorry only letter in alphabet please")
        generate_nato_alphabet()
    else:
        print(answer_words)
generate_nato_alphabet()




