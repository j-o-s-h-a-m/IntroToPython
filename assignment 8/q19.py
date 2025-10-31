#Author = Saksham Joshi
#date = 31/10/2025
#Write a Python program to print every integer between 1 and n divisible by m. Also report whether the number that is divisible by m is even or odd.



n = int(input('input a number for range: '))
m = int(input('Enter a number to divide: '))

for i in range(1,n):
    if i%m == 0:
        print(i)
