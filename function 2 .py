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
   
    

print(smallest)
print(largest)

raangi = largest - smallest
