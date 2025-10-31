#Author = Saksham Joshi
#date = 31/10/2025
#Write a program to input N numbers and then print the second largest number.

number = input('enter a list of numbers in the form a , b , c ,d:')
largest = number[0]


for i in number:
    if i > largest:
        largest = i
    
for val in number:
    if val < largest:
            largest2 = val

        
print(largest2)
