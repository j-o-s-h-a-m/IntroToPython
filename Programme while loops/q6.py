#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting
number = int(input('Input a number : '))
count = 0

while count != 50 :
    if count < 50 :
        number = int(input('Input a number : '))
    else :
        break
    
    count += number
    print(count)
