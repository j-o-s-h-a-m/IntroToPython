binary_number = input('Enter Your first binary Number :  ')
binary_number2 = input('Enter Your second binary Number :  ')

num1 = len(binary_number)
num2 = len(binary_number2)

if num1 > num2 :
    num3 = num2
else :
    num3 = num1
carry = 0

for i in range(-1,-num3-1,-1) :
    x = int(binary_number2[i]) + int(binary_number[i]) + carry
    if x >= 2 :
        carry = 1
        x = x-2 
    elif x < 2 :
        carry = 0
    print(x)
