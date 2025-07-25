operator = input("Enter an operator (+ - * /): ")
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the secoond number: "))

if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    result = first_num / second_num
else:
    print("Invalid operator")
    exit()

print(f"{first_num} {operator} {second_num} = {result}")