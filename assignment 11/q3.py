#Author = Saksham Joshi
#date = 31/10/2025
#Write a program to take in a string which is a mixture of characters. Extract all the digits from the string and print their total.
#Example input/output:- Input: Ab2 n4lksdf$89lkjd9%lskj f34 , Output: The sum of the digits in the string is: 39'

anything = input('enter your creation : ')
count = 0
for i in anything:
    if i.isdigit():
        i = int(i)
        count = count+i
    else:
        print(i)
print(count)
        

