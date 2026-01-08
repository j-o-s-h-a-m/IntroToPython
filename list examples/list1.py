myl = [2,4,6]
print('Existinglistis: ',myl)
n = eval(input('Enter a number or a list to be appended: '))
if type(n) == type([]) :#if a list is input
    myl.extend(n)
elif type(n) == type(1):#if an integer is input
    myl.append(n)
else:
    print('Please enter either an integer or a list.')
print('appended list is : ',myl)






