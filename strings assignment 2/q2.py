#Author = Saksham joshi
#23/10/2025
#Write a program to calculate the length of a string using :
#i) A for loop
#ii) A while loop

# A for loop
word = input('Enter Your word : ')
count = 0
for i in word:
    count += 1

print(count)

#A While loop

word = input('Enter Your word : ')
count = 0
length = len(word)

while count < length:
    count += 1

print(count)
