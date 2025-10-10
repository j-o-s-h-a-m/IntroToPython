#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program that prints from 1 to n squared using a while loop. It should stop the while loop if the iteration count is 50. (Hint use break)
number = int(input('Input a number : '))
count = 1

while count != 50 and number:
    if count <= number :
        print(count,'squared', count ,'is',count*count)
    count += 1
    if count > number:
        break
