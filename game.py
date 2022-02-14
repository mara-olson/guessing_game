"""A number-guessing game."""
from random import randint

user = input("Enter your name: ")
print("Welcome to the guessing game, {}!".format(user))
# print("Welcome to the guessing game, "+ user + "!" )
answer = randint(1, 100)

# try: 
guess = input("Enter a number between 1 and 100: ")
# except ValueError:
#   guess = int(input("That's not a number... Try adding a number between 1 and 100 this time: "))
# else: 
#   if guess < 1 or guess > 100:
#     guess = int(input("Whomp whomp. That number wasn't between 1 and 100. Try again: "))
			

# assuming the guesser inputs a number and not something random 
count = 0
while guess != answer:
	while True:
		try: 
			guess = int(guess)
		except ValueError:
			guess = int(input("That's not a number... Try adding a number between 1 and 100 this time: "))
		else:
			if guess < 1 or guess > 100:
				guess = int(input("Whomp whomp. That number wasn't between 1 and 100. Try again: "))
			elif guess < answer:
				guess = int(input("Try again, your guess is too low: "))
				count += 1
			elif guess > answer:
				guess = int(input("Try again, your guess is too high: "))
				count += 1
			else:
				print("Congratulations, after {} guesses you got it!".format(count))
