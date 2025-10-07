
number = int(input('Input a number : '))
count = 0

while count != 50 :
    if count < 50 :
        number = int(input('Input a number : '))
    else :
        break
    
    count += number
    print(count)
