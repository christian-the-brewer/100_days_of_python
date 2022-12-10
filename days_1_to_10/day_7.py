#Day 7 Hangman game

#Present user with a line of underscores representing the word.

#Only alow solution guesses that are the same length of word, otherwise only allow single char

#Replace underscores with letter in the correct place if the user guesses a correct letter

#If the letter is not contained in the word, draw the hanged man and increment a count

#When count equals the desired count, game over, otherwise continue until the word is guessed. 

 #Step 1
import random

word_list = ["aardvark", "baboon", "camel"]
correct_guesses = []
lives = 5
empty_board = ""

#randomly choose word
chosen_word = word_list[random.randint(0,len(word_list)-1)]

print(chosen_word)
for char in chosen_word:
    empty_board += "_"


#check if letter guessed is in the chosen_word and add to correct_guess if it is
def check_letter(letter, word):
    if letter in word:
        correct_guesses.append(letter)

#function to print the gameboard 
def print_blanks():
    displayed_word = ""
    for char in chosen_word:
        if char in correct_guesses:
            displayed_word += char
        else:
            displayed_word += "_"
    return displayed_word




print("Hangman 2: Hang In There!")
print(empty_board)
while lives > 0:
    #ask user to guess a letter, store as guess variable and make lowercase
    guess = input("Guess a letter!\n").lower()

    check_letter(guess, chosen_word)

    print_blanks()