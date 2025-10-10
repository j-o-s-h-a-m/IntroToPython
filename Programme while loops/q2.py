#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program that takes test grades from the user and returns their average and the letter grade of the average. Use a while loop and make negative number the stop criteria. A >=90 B 80-89 C 70-79 D 60-69 F 59 or less
number = 2
total = 0
count = 0

while number != '':
    number = input('Enter your percentage for each subject: ')
    if number.isdigit():
        number = int(number)
        total += number
        count += 1
        average = total/count
        
print(average)

if (average >= 90):
    print('Your Grade is A')
elif (average<=89) and (average>=80):
    print('Your grade is B')
elif (average>=79) and (average<= 70):
    print('your grade is c')
elif (average>=60) and (average<= 69):
    print('your grade is d')
else:
    print('your grade is f')
