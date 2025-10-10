#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program which asks the user to guess a value you have set in your code. The program should tell them if their guess is too high or too low and print a well done message when they guess it correct telling them how many attempts it took.
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
