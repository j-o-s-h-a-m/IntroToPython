#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting
wn = 1
total = 0

while wn != '' :
    number = int(input('Enter your number : '))
    if number == 20 :
        print('Bang On')
        break
    elif number < 20 :
        print('Too Low')
    elif number > 20 :
        print('Too High')
    total += 1

print('it took you',total,'times to get it')
