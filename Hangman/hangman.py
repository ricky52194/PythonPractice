import random
import hangman_words
import hangman_art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = hangman_words.word_list
print(hangman_art.logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(word_length):
    display += "_"

used_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Create used letter bank
    if guess in used_letters:
        print("You have used this letter before. Guess again!")
    elif len(guess) > 1:
        print("Select only one letter. Guess again!")
    else:
        used_letters.append(guess)
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # TODO-2: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"You have {lives} lives left!")
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
