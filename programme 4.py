#Athor = Saksham Joshi
#Date = 1st of Semptember 2025
#description = Program to request user name as input and return the same with a greeting 
total_slices = input('Total Number of pizza slices : ')
total_slices = int(total_slices)

slices_eaten = input('Number Of slices You ate : ')
slices_eaten = int(slices_eaten)
total_slices = total_slices - slices_eaten

print(total_slices)
