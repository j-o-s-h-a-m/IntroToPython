#Author = Saksham Joshi
#date = 31/10/25
#Write a program which asks the user to guess a number between 1 and 100 inclusive. You can hardcode the number they are trying to guess. Prompt the user if they
#are too high or too low. They can have no more than 7 attempts. If they use more then 7
#print ‘Game Over’ and tell them the answer.

count = 0

while count != 7 :
    number = int(input('guess and enter the number that i am thinking between 1 and 100 inclusive : '))
    count += 1
    if number > 7 :
        print('Too High')
    elif number < 7 :
        print('too low')
    elif number == 7:
        print('thats my number')
        break
if number != 7 :
    print('game over, The answer is 7')
    
