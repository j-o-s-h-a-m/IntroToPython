number = input('enter a list of numbers in the form a , b , c ,d:')
largest = number[0]

for i in number:
    if i > largest:
        largest = i
        
print(i)
