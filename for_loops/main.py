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