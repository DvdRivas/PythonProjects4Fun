#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Names/invited_names.txt") as invited:
    names = invited.readlines()
for n in range(0,len(names)):
    names[n] = names[n].strip("\n")

with open("Input/Letters/starting_letter.txt") as letter:
    carta = letter.read()
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt","w") as new_letter:
            new_letter.write(carta.replace("[name]",name))
