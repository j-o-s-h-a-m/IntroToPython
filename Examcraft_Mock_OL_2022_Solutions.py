# ============================================================
# Examcraft Mock Pre-Leaving Certificate 2022 - Ordinary Level
# Computer Science Section C - Programming Solutions
# ============================================================


# ------------------------------------------------------------
# Question 16(a) - Quadrilateral Perimeter and Area Calculator
# ------------------------------------------------------------

# Part (i) - Descriptive message at the start
print("This program can find the perimeter or area of a quadrilateral")

# Part (iii) - User inputs length and width as floats
length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

# Part (ii) - Ask for user name
name = input("Please enter your user name: ")

choice = input("Do you want to find the (p)erimeter or (a)rea? ")

if choice == "p":
    # Part (vi) - Use formula: (2 x length) + (2 x width)
    perimeter = (2 * length) + (2 * width)
    # Parts (iv) and (v) - Round to 2 dp, informative output
    print(f"A quadrilateral with a length of {length} and a width of {width} has a perimeter of: {round(perimeter, 2)}")

elif choice == "a":
    area = length * width
    # Parts (iv) and (v) - Round to 2 dp, informative output
    print(f"A quadrilateral with a length of {length} and a width of {width} has an area of: {round(area, 2)}")

print(f"Thank you for using the program {name}")


# ------------------------------------------------------------
# Question 16(b) - Rock Paper Scissors Game
# ------------------------------------------------------------

import random

computer_options = ["rock", "paper", "scissors"]
computer_choice = computer_options[random.randint(0, 2)]

# Part (i) - Get player's choice and print both choices
player_choice = input("Enter rock, paper or scissors: ")
print("Player chose:", player_choice)
print("Computer chose:", computer_choice)

# Part (ii) - Determine and print the winner
if player_choice == computer_choice:
    print("Draw!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("Player wins")
else:
    print("Computer wins")
