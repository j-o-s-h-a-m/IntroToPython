#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program to enter numbers until the user enters 0. Then it should print the count of the positive and negative numbers entered. You can assume all input is numeric.

n =  2
total = 0
number =  input('Enter Your Number: ')
number = int(number)


while number != 0:
    remainder = number%2
    print(remainder)
    number = number//2
