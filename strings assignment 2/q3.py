#Author = Saksham Joshi
#23/10/2025
#Create a string from a given string where all occurrences of its first character have been changed to '$', except the first char itself

variable = input('Enter Your word: ')
v1 = variable[0]
v2 = variable[1:]
v3 = v2.replace(v1,'$')
print(v1 + v3)
