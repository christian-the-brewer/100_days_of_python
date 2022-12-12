#Day 7 Hangman game

#Present user with a line of underscores representing the word.

#Only alow solution guesses that are the same length of word, otherwise only allow single char

#Replace underscores with letter in the correct place if the user guesses a correct letter

#If the letter is not contained in the word, draw the hanged man and increment a count

#When count equals the desired count, game over, otherwise continue until the word is guessed. 

 #Step 1
import random
import hangman_wordlist

# word_list = ["aardvark", "baboon", "camel"]
correct_guesses = []
lives = 5
game_won = False

#randomly choose word
chosen_word = 

print(chosen_word)

#check if letter guessed is in the chosen_word and add to correct_guess if it is
def check_letter(letter, word):
    global lives
    if letter in word:
        correct_guesses.append(letter)
    else:
        lives -= 1

#function to print the gameboard 
def print_blanks():
    global game_won
    displayed_word = ""
    for char in chosen_word:
        if char in correct_guesses:
            displayed_word += char
        else:
            displayed_word += "_"
    #determine win state by checking if the displayed_word contains any underscores
    if "_" not in displayed_word:
        game_won = True 
    return displayed_word




print("Hangman 2: Hang In There!")

while lives > 0:
    print(print_blanks())
    
    if game_won == True:
        print(f"You win! The word was {chosen_word}.")
        break
    #ask user to guess a letter, store as guess variable and make lowercase
    guess = input("Guess a letter!\n").lower()

    check_letter(guess, chosen_word)
    if chosen_word.split() in correct_guesses:
        game_won = True
    #If lives reach 0 and no win condition has been found end game with you lsot and display word

if game_won == False:
    print(f"You lose! The word was {chosen_word}!")
      
   
    

    

