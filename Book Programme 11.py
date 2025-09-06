#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting 
p = input('enter Principal : ')
p = float(p)
r = input('Enter rate of interest : ')
r = float(r)
t = input('Enter time : ')
t = float(t)
n = input('Enter the number of times interest is compounded : ')
n = float(n)
simple_interest = p*r*t
compound_interest = p*(1 + r/n)**(n/t)
print('simple_interest is : ',simple_interest,'and compound interest is',compound_interest)
