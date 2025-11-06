#Author = Saksham Joshi
#Date = 3/11/2008
#write a program to input a fromula to check if the formula has the number of opening bracekts and closing brackets

x = input('Enter a string with open and closed brackets: ')
b_o = 0
b_p = 0 
for i in x :
    if i == '(' :
        b_o += 1
    elif i == ')' :
        b_p += 1
    
if b_o == b_p :
    print('same number of brackets')
elif b_p != b_p :
    print('the number of brackets are not same')
