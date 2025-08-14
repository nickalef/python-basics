keypad = ((1, 2, 3), 
          (4, 5, 6), 
          (7, 8, 9), 
          ("*", 0, "#"))

for collection in keypad:
    for key in collection:
        print(key, end=" ")
    print()