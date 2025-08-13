fruits = ["apple", "orange", "banana", "coconut"]
veggies = ("carrot", "broccoli", "potato")


print(len(fruits))
print("apple" in fruits) # Boolean result
print(fruits.index("apple")) # int result
fruits[1] = "pineapple" # reassignment
print(fruits)

fruits.append("strawberry")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(2, "potato")
print(fruits)
fruits.extend(veggies) # So this actually goes through an iterable and adds them to the list.
print(fruits)
fruits.insert(len(fruits), veggies) # This just shoves the tuple into the list.
print(fruits)
fruits.append(veggies) # does the same thing as insert.
print(fruits)
fruits.remove(veggies)
fruits.remove(veggies)
fruits.sort() # does not work with things like tuples only strings
print(fruits)