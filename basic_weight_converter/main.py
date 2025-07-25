weight = float(input("Enter your weight: "))
unit = input("Is this your weight in pounds or kilograms (P or K): ")

if unit.upper() == "P":
    weight /= 2.205
    unit = "kgs"
elif unit.upper() == "K":
    weight *= 2.205
    unit = "lbs"
else:
    print(f"{unit} is not valid.")
    exit()

print(f"You weigh {round(weight, 2)} {unit}.")