from random import randint

greeting = print("Welcome to the game!")
player_name = input("Please enter your name: ")


def generate_random_number():
    while True:
        answer = randint(1, 100)
        guess_count = 1
        scores = []
        guess = int(input("Please enter a number between 1 and 100: "))

        while guess != answer:
            if guess < 1 or guess > 100:
                guess = int(input(f"Hey dumb-bumb, that's not a number between 1 and 100. You've now guessed {guess_count} times. Try again: "))
                guess_count += 1
            elif guess < answer:
                guess = int(input(f"Ah, too low. You've now guessed {guess_count} times. Try again: "))
                guess_count += 1
            else:
                guess = int(input(f"Ah, too high. You've now guessed {guess_count} times. Try again: "))
                guess_count += 1
        
        scores.append(guess_count)
        
        high_score = min(scores) 

        print(f'Well done! You got the correct answer after guessing {guess_count} times. Your high score is {high_score}')

        play_again = input("Would you like to play again? Y/N: ")

        if play_again != 'Y':
            print("Thanks for playing!")
            break

generate_random_number()
