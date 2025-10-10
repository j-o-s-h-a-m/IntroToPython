#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program which takes in a numbers from the user. It should continue taking in numbers until the total of all the numbers entered is greater than 50.
number = int(input('Input a number : '))
count = 0

while count != 50 :
    if count < 50 :
        number = int(input('Input a number : '))
    else :
        break
    
    count += number
    print(count)
