#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program that takes an integer number and outputs all the even numbers starting from 0 to the number
number = int(input('Input a number : '))
count = 0

while count <= number:
    if count%2 == 0:
        print(count)
    count += 1
