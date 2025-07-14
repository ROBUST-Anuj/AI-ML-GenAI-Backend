import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
lett = []
for n in range(0,nr_letters):
 lett.append(random.choice(letters))
 password = password + lett[n]

sym = []
for n in range(0, nr_symbols):
 sym.append(random.choice(symbols))
 password = password + sym[n]


num = []
for n in range(0, nr_numbers):
 num.append(random.choice(numbers))
 password = password + num[n]

print(password)


password1 = []
password_hard = ""

for n in range(0,nr_letters):
 password1.append(random.choice(lett))

for n in range(0, nr_symbols):
 password1.append(random.choice(symbols))

for n in range(0, nr_numbers):
 password1.append(random.choice(numbers))

random.shuffle(password1)
for n in range(0,(nr_numbers + nr_symbols + nr_letters)):
 password_hard =  password_hard + password1[n]

print(password_hard)
