#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting
wn = 1

while wn != '' :
    number = int(input('Enter your number : '))
    if number >= 10 and number <= 20 :
        print('thank you')
        break
    elif number < 10 :
        print('Too Low')
    elif number > 20 :
        print('Too High')
