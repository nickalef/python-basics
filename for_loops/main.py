import random

list_one = [1, 2, 3, 4, 5]
count = len(list_one)
print(count)


for index in range(count):
    print(index)
    print(list_one)
    list_one.append(random.randrange(1, 10))
    print(f"Added {list_one[-1]}")
    
list_one.sort()
print(f"Sorted list: {list_one}")

list_two = [1, 2, 3, 4, 5]
count = len(list_two)
print(count)

for index in range(count):
    print(f"index: {index}")
    for index2 in range(count):
        print(f"nested index: {index}")
        print(f"nested index2: {index2}")

for j in range(3):
    for i in range(1, 10):
        print(i, end="")
    print()

rows = int(input("Enter the number of rows you want the rectangle to have: "))
cols = int(input("Same with columns: "))

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()