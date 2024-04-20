############### Blackjack Project #####################
import random
import os
from art import logo


def deal_card():
    """returns random card picked from deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_cards):
    """calculate score of provided list of cards"""
    if 11 in list_cards and sum(list_cards) > 21:
        list_cards.remove(11)
        list_cards.append(1)

    if len(list_cards) == 2 and sum(list_cards) == 21:  # check for a blackjack
        return 0

    return sum(list_cards)


def compare(user_score, computer_score):
    """function to compare and choose winner bases on user_score and computer_score"""
    if computer_score == user_score:
        return "Draw :0"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack."
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over, You Lose"
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


# ======== STARTS HERE ===================
def play_game():
    """function to start the blackjack game until user option for it by giving input 'y'"""
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_hit == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # compares and choose winner


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()
