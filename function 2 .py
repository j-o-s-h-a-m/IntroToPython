#Author = Saksham Joshi

n = (input('enter value : '))
lst = eval(n)
lst = list(lst)
print(lst)
largest = lst[0] 
smallest = lst[0]

for i in lst:
    if i > largest :
        largest = i
    if i < smallest :
        smallest = i
   
    

print(int(smallest))
print(int(largest))

raangi = largest - smallest

n = len(lst)
if n%2 == 0:
    median = (n+1)/2
elif n%2 != 0:
    median = ((n/2) + ((n/2)+1))/2

print(median)

