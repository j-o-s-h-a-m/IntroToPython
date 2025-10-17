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
