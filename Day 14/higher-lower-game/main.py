from game_data import data
from art import logo
from art import vs
import random
import os


def fetch_object():
    """returns random dictionary reffered as object from a list of data of celebrities"""
    object = random.choice(data)
    return object


def show_account(object):
    """shows account of given object"""
    return f"{object['name']}, a {object['description']}, from {object['country']}"


def compare_followers(objectA, objectB):
    """returns the object which has more followers"""
    if objectA["follower_count"] > objectB["follower_count"]:
        return "A"
    else:
        return "B"


# =================================================================
def game():
    os.system("cls")
    is_game_on = True
    score = 0
    print(logo)

    while is_game_on != False:
        if score == 0:
            objectA = fetch_object()
        objectB = fetch_object()
        if objectA == objectB:
            objectB = random.choice(data)

        print(
            f"Compare A: {show_account(objectA)}\n{vs}\nAgainst B: {show_account(objectB)}"
        )
        user_choice = input("Who has more followers? Type 'A' or 'B':").capitalize()
        max_followers = compare_followers(objectA, objectB)

        if max_followers == user_choice:
            score += 1
            os.system("cls")
            print(logo)
            print(f"You're right! Current score: {score}.")
            objectA = objectB
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            is_game_on = False


game()
