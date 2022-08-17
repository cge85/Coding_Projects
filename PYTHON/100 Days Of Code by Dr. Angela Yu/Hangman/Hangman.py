import random
from Hangman_art import stages, logo
from Hangman_words import word_list
import os

clear = lambda: os.system('cls')

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
end_of_game = False
word_length = len(chosen_word)
lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty list for each letter of chosen_word.
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
# User input for guessed letter
    guess = input("Guess a letter: ").lower()

    clear()
    print(logo)

    if guess in display:
        print(f'You have already guessed the letter "{guess}"')
# Check if letter is in the chosen word and replace the position with the letter coresponding to that position.
    for position in range(word_length):
        letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f'The letter "{guess}" is not in the word. You have lost a life, {lives} life remaining!')
        if lives == 0:
            end_of_game = True
            print("You lose") 

    print(f"{' '.join(display)}")
    

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])
