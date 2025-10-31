#Author = Saksham Joshi
#date = 31/10/2025
#Ask the user to enter a word and print the word modified as follows:
#• If the first letter of the word is a vowel, add ‘way’ to the end. So, if the user enters
#‘apple’ it should output ‘appleway’.
#• If the first letter of the word is a consonant, move the first letter to the end and
#add ‘ay’. So, if the user enters ‘pear’, it should output ‘earpay’.
word = input('enter your world: ')
y = len(word)
n = 1 

if word[0] in 'aeiou':
  print(word + 'way')
else :
  wordnew = ''
  for i in range (1, len(word)) :
      wordnew = wordnew + word[i]
  wordnew = wordnew + word[0]
  print(wordnew + 'ay')
