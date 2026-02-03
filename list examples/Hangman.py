word = 'sauce'
blank = ''
for i in word:
    blank += ' _'
n = 0
y = ''
tries = 20
pos = 0
count = 0
while n == 0 :
    print(blank)
    print('tries left :',tries)
    char = input('enter a character: ')
    y += char
    if char in word:
        print('letter is in the secret word')
        pos = word.index(char)
    elif char in blank :
        print('the letter has already been guessed')
    else :
        print('the Letter is not in the secret word')
        tries -= 1
    for i in word:
        if count == pos :
            blank += i
        else :
            blank += '_'
    
    


