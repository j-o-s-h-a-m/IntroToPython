#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting 


user_fname = input('First Name : ')
user_Surname = input('Surname Name : ')
print('Hello,' , user_fname, user_Surname)

x = input('Enter Your First Number :  ')
x = int(x)
y = input('Enter Your Second name  :  ')
y = int(y)
total = x + y
print(total)
 
First_number = input(' first Number : ')
First_number = int(First_number)

Second_number = input('Second Number : ')
Second_number = int(Second_number)
third_number = input('Third number :  ')
third_number = int(third_number)

total2 = First_number + Second_number + third_number
total3 = total + total2

print(total3)

total_slices = input('Total Number of pizza slices : ')
total_slices = int(total_slices)

slices_eaten = input('Number Of slices You ate : ')
slices_eaten = int(slices_eaten)
total_slices = total_slices - slices_eaten
print(total_slices)

name = input('enter your name : ')
age = input('enter your age : ')
age = int(age)

age_next_year = age + 1

print('hello,',name,', next year you will be',age_next_year)

total_bill = input('Enter total Bill : ')
total_bill = int(total_bill)

no_diners = input('Number of diners : ')
no_diners = int(no_dineers)
each_p = total_bill/no_diners
print('Each person should pay',each_p)

no_days = input('enter a random number of days : ')
no_days = int(no_days)
hours = no_days*24
minutes = no_days*24*60
seconds = no_days*24*60*60

if no_days > 1 :
 print('there are',hours,'hours',minutes,'minutes and',seconds,'seconds in',no_days,'days')
else :
 print('there are',hours,'hours',minutes,'minutes and',seconds,'seconds in a day')

pounds_lbs = input('Enter Wweight in pounds : ')
pounds_lbs = int(pounds_lbs)

kgs = pounds_lbs*2.204

print('there are',kgs,'kilograms in',pounds_lbs,'pounds')

          


