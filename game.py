
from random import randint

"""A number-guessing game."""

attempts = 0
number = randint(1, 100)

greeting = input("Welcome to our guessing game! What is your name? > ")
greeting = greeting.title()

print(f"Hello {greeting}, I'm thinking of a number between 1 and 100")
print("Try to guess my number")

"""Asks player to guess a random number""" 

while True:
    guess = input("Your guess? > ")

    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}"is not a valid number, try again')
        continue

    if guess < 1 and guess > 100:
        print("Please guess a number between 1 and 100")

    attempts += 1

    if guess < number:
        print("Your guess is too low, try again")

    elif guess > number:
        print("Your guess is too high, try again")

    else:
        print(f"Well done, {greeting}!")
        print(f"You found my number is {attempts} attempts")
        break



