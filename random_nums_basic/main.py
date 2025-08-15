import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

die = random.randint(low, high) # inclusive random number from low to high
print(die)

number = random.random() # random floating number between 0 - 1.0
print(number)

option = random.choice(options) # Choose a random element from a non-empty sequence.
print(option)

random.shuffle(cards) # Shuffle list x in place, and return None.
print(cards)

help(random)