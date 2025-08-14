foods = []
prices = []
total = 0

while True:
    food = input("What food would you like to buy (q to quit): ")

    if food.lower() == "q":
        break

    price = float(input(f"What is the price of {food}: $"))

    foods.append(food)
    prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Total: ${total}")

for food, price in zip(foods, prices): # Looked up if for loop could have multiple iterables and found zip(). This is more for I wanted them both on one line so this part of the program can be ignored.
    print(f"{food} : ${price}")