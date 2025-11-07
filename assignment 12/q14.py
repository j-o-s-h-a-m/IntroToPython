x = input('Enter a string single spaces only : ')

count = 0
maximum = 0 

for i in x :
    if i != ' ' :
        count += 1
    elif i == ' ':
        if count > maximum :
            maximum = count
            print(x[count])
        new_v += i 
            
            
        count = 0 

print(maximum)
