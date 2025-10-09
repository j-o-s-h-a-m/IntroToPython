#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting
number = int(input('Input a number : '))
count = 1

while count <= number:
    if count%5 != 0:
        print(count)
    count += 1
