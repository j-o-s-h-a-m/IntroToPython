#Author = Saksham Joshi
#23/10/2025
#. Write a program to reverse a string using:
#• A for loop
#• A while loop
#• Slicing

# a for loop
string = input('Enter Your string : ')
empty = ''
for i in string:
    empty = i+empty
    
print(empty)

#A for while loop
string = input('Enter Your string : ')
empty = ''
count = len(string)
while count >= 0  :
    i = string[count:] + empty
    count -= 1
print(i)
