#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Write a program that prints from 1 to n using a while loop, it should skip every multiple of 5. (Hint, use % and continue)
number = int(input('Input a number : '))
count = 1

while count <= number:
    if count%5 != 0:
        print(count)
    count += 1
