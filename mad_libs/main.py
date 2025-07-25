print("Welcome to Mad Libs")

name = input("Please enter your name: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb: ")
adj = input("Please enter an adjective: ")
num = 0

while num < 1 or num > 10:
    num = int(input("Please input a number from 1-10: "))

print(f"Here is your story {name}!")
print(f"{noun} sat upon his porch thinking about {verb} the {adj} tree.")
print(f"It was {num} A.M. so {noun} decided that it was the perfect time to {verb} the {adj} tree.")