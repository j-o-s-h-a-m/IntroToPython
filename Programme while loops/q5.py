
number = int(input('Input a number : '))
count = 1

while count != 50 and number:
    if count <= number :
        print(count,'squared', count ,'is',count*count)
    count += 1
    if count > number:
        break
