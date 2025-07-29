principle = 0
interest_rate = 0
time_years = 0

while principle <= 0:
    principle = float(input("Enter your initial principal investment: "))
    if principle <= 0:
        print("Principal can't be less than or equal to zero. Try again.")

while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate: "))
    if interest_rate <= 0:
        print("Interest rate can't be less than or equal to zero. Try again.")

while time_years <= 0:
    time_years = int(input("Enter the amount of time in years: "))
    if time_years <= 0:
        print("Time can't be less than or equal to zero. Try again.")

print(principle)
print(interest_rate)
print(time_years)