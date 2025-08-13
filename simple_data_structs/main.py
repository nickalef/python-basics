fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[:4])
print(fruits[::-1])

for i in fruits:
    print(i)
    for j in fruits:
        print(j, end=" ")
    print()
    