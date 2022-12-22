import pandas

data = pandas.read_csv("nato_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_reading = True
while is_reading:
  ask_user = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in ask_user]
  except KeyError:
    print("Sorry only Alphabets are allowed")
    is_reading = True
  else:
    print(output_list)
    is_reading = False
