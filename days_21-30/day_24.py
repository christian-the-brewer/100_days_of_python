#Day 24
#mail merger
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./mail_merger/letters/starting_text.txt", "r") as form:
    letter_form = form.read()
    print(letter_form)

with open("./mail_merger/names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
    print(names)
    
invites = []

for name in names:
    new_invite = letter_form.replace("[name]", name.strip())
    invites.append(new_invite)


