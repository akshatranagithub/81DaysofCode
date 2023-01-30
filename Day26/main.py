import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[letter] for letter in name if letter.isalpha()]
    except KeyError:
        print("Please use letters only in the word")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
