
n =  2
total = 0


while n != '':
    number =  input('Enter Your Number: ')
    number.isdigit()
    number = int(number)
    if number == 0 or number == ''  :
        break
    total += number

print(total)
