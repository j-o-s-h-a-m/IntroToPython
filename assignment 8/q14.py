#Author = Saksham Joshi
#date = 31/10/2025
#Write a program to take N (N > 20) as an input from the user. Print numbers from 11 to N. When the
#number is a multiple of 3, print "Tipsy", when it is a multiple of 7, print "Topsy". When it is a multiple
#of both, print "TipsyTopsy".
x = int(input('enter a number less than 20 : '))

if x%3 == 0 and x%7 == 0:
    print('tipsytopsy')
elif x%7 == 0:
    print('topsy')
elif x%3 == 0 :
    print('tipsy')

