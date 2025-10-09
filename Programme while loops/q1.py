#Athor = Saksham Joshi
#Date = 7st of october 2025
#description = Program to request user to input scores of their subject and return the average 

n = -1 #enter your default value
total = 0 
count = 0
while n!='' :
  n = input('enter your number: ')
  if n.isdigit():
    total += int(n)
    count += 1
print('average is: ', total/count)

total = total + int(n)
    
