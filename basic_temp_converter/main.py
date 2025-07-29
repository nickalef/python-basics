temp = float(input("Please input a temperature: "))
type = input(f"Is {temp} temperature in fahrenheit or celsius (input either 'F' or 'C'): ")

if type.upper() == 'F':
    converted_temp = (temp - 32) / (9/5)
    print(f"{temp}°F -> {converted_temp:.0f}°C")
elif type.upper() == 'C':
    converted_temp = (temp * (9/5)) + 32
    print(f"{temp}°C -> {converted_temp:.0f}°F")
else:
    print(f"{type} is not valid!")