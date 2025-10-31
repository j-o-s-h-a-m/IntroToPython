#Author = Saksham Joshi
#date = 31/10/2025
#Write a program to count the number of times a character occurs in the given string.The string and the character should be input by the user.

word = input(' enter a word of your choice : ')
letter = input('enter a letter of your choice : ')
count = 0

for i in word:
  if i == letter:
    count += 1
print('The letter',letter,'occurs the following times : ',count)
