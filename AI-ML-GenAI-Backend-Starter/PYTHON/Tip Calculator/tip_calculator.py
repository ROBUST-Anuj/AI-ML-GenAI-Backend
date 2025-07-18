print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
s_bill = (bill + (tip*bill)/100)/people
print(f"Each person should pay{s_bill}")