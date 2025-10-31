#Author = Saksham Joshi
#date = 31/10/2025
#Write a complete Python program to do the following:
#(i) read an integer Х. (ii) determine the number of digits n in X.
#(iii) form an integer Y that has the number of digits n at ten's place and the most significant digit of X
#at one's place. (iv) Output Y.
x = input('input an integer : ')
n = str(len(x))

x = x[0]
y = n + x
print(y)
