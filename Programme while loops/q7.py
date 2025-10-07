wn = 1

while wn != '' :
    number = int(input('Enter your number : '))
    if number >= 10 and number <= 20 :
        print('thank you')
        break
    elif number < 10 :
        print('Too Low')
    elif number > 20 :
        print('Too High')
