lst1 = eval(input('Enter a number between 1 and 12 : '))
lst1 = list(lst1)
count = 0
print(lst1)
for i in lst1 :
  if int(i) > 10 :
    lst1[count] = 10
  count += 1 
print(lst1)
