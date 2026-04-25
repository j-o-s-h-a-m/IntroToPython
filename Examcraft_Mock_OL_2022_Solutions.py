


print("This program can find the perimeter or area of a quadrilateral")

length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

name = input("Please enter your user name: ")

choice = input("Do you want to find the (p)erimeter or (a)rea? ")

if choice == "p":
    perimeter = (2 * length) + (2 * width)
    print(f"A quadrilateral with a length of {length} and a width of {width} has a perimeter of: {round(perimeter, 2)}")

elif choice == "a":
    area = length * width
    print(f"A quadrilateral with a length of {length} and a width of {width} has an area of: {round(area, 2)}")

print(f"Thank you for using the program {name}")



import random

computer_options = ["rock", "paper", "scissors"]
computer_choice = computer_options[random.randint(0, 2)]

player_choice = input("Enter rock, paper or scissors: ")
print("Player chose:", player_choice)
print("Computer chose:", computer_choice)

if player_choice == computer_choice:
    print("Draw!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("Player wins")
else:
    print("Computer wins")
