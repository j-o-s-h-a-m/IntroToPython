#Author = Saksham Joshi
#date = 31/10/2025
#Write a short program to find largest number of a list of numbers entered through keyboard.
number = input('enter a list of numbers in the form a , b , c ,d:')
largest = number[0]

for i in number:
    if i > largest:
        largest = i
        
print(i)
