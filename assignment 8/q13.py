#Author = Saksham Joshi
#date = 31/10/2025
#Write a program to take an integer a as an input and check whether it ends with 4 or 8. If it ends with 4,print "ends with 4", if it ends with 8, print "ends with 8", otherwise print "ends with neither".

a =  input('Enter Your Number: ')

for i in a:
    i = int(i)
if i == 4 :
    print('ends with 4')
elif i == 8:
    print('ends with 8')
else:
    print('ends with niether')
