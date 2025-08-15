import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("----- NUMEROUS NUMBERS GUESSING GAME -----")
while is_running:
    try:
        user_guess = int(input(f"Select a number between {lowest_num} and {highest_num}: "))

        if user_guess < lowest_num or user_guess > highest_num:
            print("Invalid Guess")
            continue

        guesses += 1

        if user_guess == answer:
            is_running = False
            print("CORRECT!")
        elif user_guess < answer:
            print("GUESS TOO LOW! TRY AGAIN!")
        elif user_guess > answer:
            print("GUESS TOO HIGH! TRY AGAIN!")
    except ValueError:
        print("Invalid Guess!")

print(f"CONGRATS! YOU DID IT! IT TOOK YOU {guesses} GUESSES TO GUESS {answer}!")