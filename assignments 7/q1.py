#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program to check if a number is an Armstrong number. An Armstrong 
#number is a number equal to the sum of each digit raised to the power of the 
#number of digits..
wn = 1

number =  input('Enter Your Number: ')
total = 0
y = len(number)
y = int(y)


for i in number:
    i = int(i)
    i = i**y
    total += i 
    
if total == number :
    print('This number is an armstrong number')
else :
    print('Think about your life decisions')
