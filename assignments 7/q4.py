#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program to convert Decimal to Binary. Don’t worry if the answer is in reverse, we will see how to fix this soon

n =  2
total = 0
number =  input('Enter Your Number: ')
number = int(number)


while number != 0:
    remainder = number%2
    print(remainder)
    number = number//2
