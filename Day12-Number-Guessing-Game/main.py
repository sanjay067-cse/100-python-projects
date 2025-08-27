import random
from art import logo

def hard(n) :
    game_over = False
    attempts = 5
    i = 0
    while not game_over:

        attempts_left = attempts - i

        if attempts_left > 0 :
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if attempts_left > 0 :
                if attempts_left == 1 :
                    if guess != n :
                        print("You've run out of guesses. Refresh the page to run again.")
                        game_over = True

                elif guess < n :
                    print("Too Low.")
                    print("Guess again.")
                elif guess > n :
                    print("Too High.")
                    print("Guess again.")
                else :
                    print(f"You got it! The answer was {n}")
                    game_over = True

        i += 1


def easy(n) :
    game_over = False
    attempts = 10
    i = 0
    while not game_over:

        attempts_left = attempts - i

        if attempts_left > 0:
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if attempts_left > 0:
                if attempts_left == 1:
                    if guess != n:
                        print("You've run out of guesses. Refresh the page to run again.")
                        game_over = True

                elif guess < n:
                    print("Too Low.")
                    print("Guess again.")
                elif guess > n:
                    print("Too High.")
                    print("Guess again.")
                else:
                    print(f"You got it! The answer was {n}.")
                    game_over = True

        i += 1


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
num_to_guess = random.randint(1,100)
if difficulty == "hard" :
    hard(num_to_guess)
elif difficulty == "easy" :
    easy(num_to_guess)

else :
    print("Wrong Input")
