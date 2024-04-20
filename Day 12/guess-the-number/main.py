from art import logo
import random

attempts = ""

print(logo)


def have_attempts():
    global attempts
    if attempts <= 0:
        False
    else:
        True


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    global attempts
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5


def check_results(guess, random_guess):
    global attempts
    if guess == random_guess:
        print(f"You got it! The answer was {random_guess}.")
    elif guess > random_guess:
        print("Too high.")
        if have_attempts() == True:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

    elif guess < random_guess:
        print("Too low.")
        if have_attempts() == True:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")


print("I'm thinking of a number between 1 and 100.")
random_guess = random.randint(1, 100)
print(f"pssst, solution = {random_guess}")
set_difficulty()
print(f"psst, attempts = {attempts}")
guess = ""
while attempts > 0 and guess != random_guess:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    check_results(guess, random_guess)
