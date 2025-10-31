#Author = Saksham Joshi
#date = 31/10/2025
#Ask the user to enter their first name and display the length of their name
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
