import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in name if letter.isalpha()]
print(output_list)
