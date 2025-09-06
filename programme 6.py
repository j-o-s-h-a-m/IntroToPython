#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting 
total_bill = input('Enter total Bill : ')
total_bill = int(total_bill)

no_diners = input('Number of diners : ')
no_diners = int(no_diners)
each_p = total_bill/no_diners
print('Each person should pay',each_p)

