print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill = 0
if size == "S":
    bill = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    bill = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3

elif size == "L":
    bill = 25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3

else:
    print("Please place an order")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is: ${bill}.")