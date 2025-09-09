#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting 
no_days = input('enter a random number of days : ')
no_days = int(no_days)
hours = no_days*24
minutes = no_days*24*60
seconds = no_days*24*60*60

if no_days > 1 :
 print('there are',hours,'hours',minutes,'minutes and',seconds,'seconds in',no_days,'days')
else :
 print('there are',hours,'hours',minutes,'minutes and',seconds,'seconds in a day')

