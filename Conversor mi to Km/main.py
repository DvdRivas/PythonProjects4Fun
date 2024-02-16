import pandas
Error=True
while Error:
    dicc = pandas.read_csv("nato_phonetic_alphabet.csv")
    name = list(input("Type a word: ").upper())
    lista = {row.letter: row.code for (_, row) in dicc.iterrows()}
    #Loop through rows of a data frame
    try:
        nato_list = [lista[letter] for letter in name]
    except:
        print("Please introduce a valid word")
    else:
        print(nato_list)
        Error = False

    #Access index and row
    #Access row.student or row.score
 #   pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



