word = 'saauce'
pos = 0
blank=''
n = 0
tries = 20
count = 0 
# Blank
for y in word:
    blank += '_'

#User Interface 
while n == 0:
    print(blank)
    char = input('Enter a letter : ')
    y += char
    for i in word:
        if count < len(word):
            if char == i and char is not in y :
                print('Charracter found at position ',pos)
                blank = blank[0:pos] +char + blank[pos+1:]
                tries -= 1
                count += 1
            elif char in y :
                print('letter already picked')
                tries -= 1
            else:
                print('Letter is not in the word')
                tries -= 1
        pos = pos+1
        pos = 0 
    
    
