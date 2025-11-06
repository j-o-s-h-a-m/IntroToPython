#Author = Saksham Joshi
#Date = 3/11/2008
#write a program to count  a number of vowels 

x = input('Enter a string : ')
vowels = 0
for i in x :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
    
print('There are',vowels,'vowels in this string')
