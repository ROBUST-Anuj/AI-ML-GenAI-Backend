rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
# game = ["Rock","Paper","Scissors"]
user_input = int(input("Enter 0 for Rock , 1 for Paper , 2 for Scissors: "))
if user_input == 0 :
    print("You Choose Rock")
    print(rock)
elif user_input == 1 :
    print("You Choose Paper")
    print(paper)
elif user_input == 2 :
    print("You Choose Scissors")
    print(scissors)
else :
    print("Invalid Input")

com_input = random.randint(0,2)

if com_input == 0 :
    print("Computer Choose Rock")
    print(rock)
elif com_input == 1 :
    print("Computer Choose Paper")
    print(paper)
elif com_input == 2 :
    print("Computer Choose Scissors")
    print(scissors)
else :
    print("Invalid Input")

if user_input == 0 and com_input == 2 or user_input == 1 and com_input == 0 or user_input == 2 and com_input == 1 :
    print("You Won !!")
elif user_input == com_input :
    print("Draw !!  Try Again")
else :
    print("Better Luck Next Time !!")
