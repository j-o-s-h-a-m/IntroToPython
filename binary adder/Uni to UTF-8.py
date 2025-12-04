x = input('Enter  An UNICODE : ').upper() 

x = x[2:len(x)+1:]
print(x)

n = 0
count = 0

for i in x :
#     x.isdigit()
#     while i != 0 :
#         r = i%2
#         i = i//2
#         print(r)


    if i == 'A' :
        n = 10
    elif i == 'B' :
        n = 11
    elif i == 'C' :
        n = 12
    elif i == 'D' :
        n = 13
    elif i == 'E' :
        n = 14
    elif i == 'F' :
        n = 15
    else :
        n = int(i)
        
    while n != 0 :
        r = n%2
        n = n//2
        r = str(r)
        print(r)
        count += 1
        if count >= 4 :
            value = value + r
        elif count 
