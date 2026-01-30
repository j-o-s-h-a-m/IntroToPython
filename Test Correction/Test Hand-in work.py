results = eval(input('Enter the list of your exam marks: '))
results = list(results)
print(results)
LoW = 0
High = 0
N = 0
total = 0
for i in results: 
    N += 1
    total += i
    print(total)
total = total/N
print('Average mark is',float(total))

if total >= 80 :
    print('You got a disticntion')
elif total >= 65 :
    print('You got a higher merit')
elif total >= 50 :
    print('You got a lower merit')
elif total >= 40 :
    print('You got a pass')
elif total < 40 :
    print('You are Unsuccessful')
val = 0
highest = 0
lowest = 0
val = 0
for i in results :
    if i > val :
        highest = i
    elif i < val :
        lowest = i
    val = i
less40 = 0
in50nd70 = 0 
for i in results:
    if i < 40 :
        less40 += 1
    elif i <= 79 and i >= 50:
        in50nd70 += 1
        
        
print('Highest mark is',highest)
print('Lowest mark is',  lowest)
print('The number of scores below 40 is',less40)
print('The number of scores between 50 and 79 is',in50nd70)


    

    


    

    
