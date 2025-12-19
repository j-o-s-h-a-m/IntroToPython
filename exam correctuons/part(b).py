#step 1
number = input('enter a number : ')
checking_digit = number[-1]
number1 = number[0:-1:-1]
numer_odd = number[1::2]
number_evem = number[0::2]
print(number1 , checking_digit)
count = 0
total = 0 

for i in numer_odd:
    i = int(i)
    i = i**2
    count += 1
    if i > 9 :
        i = int(i)
        i = i-9
        total += i
    else :
        total += i
        
