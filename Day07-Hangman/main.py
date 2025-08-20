import random
import hangman_art
import hangman_words

lives = 6

# Importing the logo from hangman_art.py and printing it at the start of the game.
print(hangman_art.logo)

#Importing world_list from hangman_words.py and randomly choosing a word from that list
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    #Message for the user if the guessed letter has been already guessed earlier
    if guess in correct_letters :
        print("You have already guessed this letter. Guess another letter.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    #Displaying the wrong guessed letter and decreasing the no. of life by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            # Displaying the correct word that was to be guessed
            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Importing the image of stages of hangman from hangman_art.py and printing it after every guess
    print(hangman_art.stages[lives])