import random

someNumber = random.randint(1,100)

lst = [ 'banana' , 'orange' , 'mango' , 'pineapple' , 'blueberry' ]
lstran = random.choice(lst)
print(lstran)
lsthot = [ 'heads' , 'tails']
hot = input('type heads or type tails : ')
ranhot = random.choice(lsthot)
if hot == ranhot :
    print(ranhot , 'You Win')
else :
    print(ranhot , 'You Loose')

tries = 7
while tries <= 7:
    print('You have',tries,'tries')
    gnum = input('Guess the number: ')
    if gnum == someNumber :
        print('Thats correct')
    else:
        if tries != 0:
            print('thats wrong')
            tries -= 1
        else :
            print('thats wrong, Good Bye')
            break

#maths quiz
q = ''
score = 0
while q != 'q' :
    print(score)
    q = input('to quit type q else type n : ')
    x = random.randint(1,100)
    y = random.randint(1,100)
    operators = [ '+' , '-' , '*' , '//' ]
    ranop = random.choice(operators)
    print(x), print(ranop) , print(y)
    ans = input('input your answer: ')
    score = 0
    if ranop == '+' :
        mans = x + y
        if ans == mans :
            print('Thats right')
            score += 1
            print(ans)
        elif ans != mans :
            print('The answer is wrong')
            print(ans)
    elif ranop == '-':
        mans = x - y
        if ans == mans :
            print('Thats right')
            print(ans)
            score += 1
        elif ans != mans :
            print('The answer is wrong')
            print(ans)
    elif ranop == '*':
        mans = x*y
        if ans == mans :
            print('Thats right')
            print(ans)
            score += 1
        elif ans != mans :
            print('The answer is wrong')
            print(ans)
    elif  ranop == '//':
        mans = x//y
        if ans == mans :
            print('Thats right')
            print(ans)
            score += 1
        elif ans != mans :
            print('The answer is wrong')
            print(ans)


        
    




