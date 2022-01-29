"""A number-guessing game."""
from random import randint

user = input("Enter your name: ")
print("Welcome to the guessing game, {}!".format(user))
# print("Welcome to the guessing game, "+ user + "!" )
answer = randint(1, 100)
guess = int(input("Enter a number between 1 and 100: "))
# assuming the guesser inputs a number and not something random 
count = 1
while guess != answer:
    if guess < answer:
        guess = int(input("Try again, your guess is too low: "))
        count += 1
    elif guess > answer:
        guess = int(input("Try again, your guess is too high: "))
        count += 1
print("Congratulations, after {} guesses you got it!".format(count))
