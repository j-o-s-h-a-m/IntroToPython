#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program which asks the user to enter a number between 10 and 20 inclusive. If they enter a number less than 10, print ‘too low’. If they enter a number greater than 20 print ‘too high’. The program should continue until they enter a value between 10 and 20 then display the message ‘Thank you’
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
