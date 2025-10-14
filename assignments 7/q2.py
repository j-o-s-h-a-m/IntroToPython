#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program to enter numbers until the user enters 0. Then it should print the count of the positive and negative numbers entered. You can assume all input is numeric.

n =  2
total = 0


while n != '':
    number =  input('Enter Your Number: ')
    number.isdigit()
    number = int(number)
    if number == 0 or number == ''  :
        break
    total += number

print(total)
