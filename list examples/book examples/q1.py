x=[1,2,4]
print(x)
increment = int(input('increment number : '))

count = 0 

for i in x:
    x[count] = i+increment
    count += +1
print(x)
