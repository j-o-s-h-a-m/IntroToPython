#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting
number = int(input('Input a number : '))
count = 1

while count != 50 and number:
    if count <= number :
        print(count,'squared', count ,'is',count*count)
    count += 1
    if count > number:
        break
