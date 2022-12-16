import pandas

data = pandas.read_csv("nato_alphabet.csv")

# Creating a dictionary from a csv file
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

ask_user = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in ask_user]
print(output_list)
