fruits =  ["apple", "orange", "banana", "coconut"]
veggies = ["celery", "carrots", "potatoes"]
meats =   ["chicken", "fish", "turkey"]

groceries = [fruits, veggies, meats]

print(groceries) # all
print(groceries[0]) # prints first list all items
print(groceries[0][2]) # prints first list second item

print("-----------------------")

for collection in groceries: # In a 2D collection first for loop prints the collection
    for food in collection: # Second loop prints the item in the collection
        print(food, end=" ")
    print()

# So the nested for loop behaves the same like when you have a range. The first collection is like index 0 (even though it is a list). Then the nested part is like "ok we have seperated the list from the 2D collection. Loop through that list." 

# OR can do below to make 2D
groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]