#Author = Saksham Joshi
#Date = 3 / 11 / 2025
x = input('Enter a string single spaces only : ')
y = len(x)
count = 0

for i in x :
    if i == ' ' :
        count += 1 

no_letters = y-count
print(no_letters)
