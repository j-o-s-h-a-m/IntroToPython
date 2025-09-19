#Athor = Saksham Joshi
#Date = 14 september 2025
#description = program to check if its a child, teenger or a adulbased on the age given by an user 
age = int(input('Enter Your age : '))

if age < 13 :
    print('child')
elif 13 <= age and age < 20 :
    print('teenager')
else :
    print('Adult')
