import random

loop_end = [1, 2, 3, 4, 5]


for index in loop_end:
    print(index)
    print(loop_end)
    loop_end.append(random.randrange(1, 10))