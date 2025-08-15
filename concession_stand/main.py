menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("-------------- MENU --------------")
print("Item")
for item, price in menu.items():
    print(f"{item:<10}... ${price:.2f}")

while True:
    user_item = input("Enter the name of the item you would like to add to your cart from the menu (q to quit): ").lower()
    
    if user_item == "q":
        break
    
    cart.append(user_item)
    total += menu.get(user_item)

print("-------------- YOUR CART --------------")
for item in cart:
    print(item)
print(f"The total cost of you cart is ${total:.2f}")