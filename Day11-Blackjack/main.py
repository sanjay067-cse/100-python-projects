import random
from art import logo             #logo of Blackjack is in art.py


def deal_card():
    """Returns a random card from the deck"""                     #Docstring (A small documentation of the above function)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""         #Docstring
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)      #Here remove() will remove 11(Ace) if 11 is in the cards and sum is greater than 21.
        cards.append(1)       #11 got removed and 1 got added in the list to check new score by keeping Ace as 1.

    return sum(cards)



def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:                                       #Here c_score=0 resembles Blackjack has been obtained by computer in first two cards: Ace(11) + 10. Therefore, Immediate Win
        return "You Lose, opponent has Blackjack 😱"
    elif u_score == 0:                                       #Here u_score=0 resembles Blackjack has been obtained by user in first two cards: Ace(11) + 10. Therefore, Immediate Win
        return "You won with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1        #Zero as an initial value has not been assigned because 0 represents Blackjack
    user_score = -1
    is_game_over = False

    for _ in range(2):         #Loop runs 2 times for 0 and 1. Here '_' is a throwaway variable. Since we don’t actually need the numbers 0 and 1, we use _ to say: I don’t care about these values.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:             # 0 implies Blackjack : Score = 21 (Ace+10)
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":  #loop runs every time the user selects 'y'.
    print("\n" * 20)
    play_game()                                                                    #i.e. User can play as many times as he wishes to.
