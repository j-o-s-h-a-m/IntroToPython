#Author = Saksham joshi
#Date = 31/10/2025
#Write a program to check if a string is a palindrome. A palindrome is a word or string
#that reads the same backwards and forwards. For example: racecar; rotator

word = input('enter your word : ')
word2 = word[::-1]

if word2 == word :
  print('its a palindrome')
else:
  print(word2)
