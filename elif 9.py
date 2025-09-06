#Athor = Saksham Joshi
#Date = 4th of Semptember 2025
#description = working with if and else commands 
units = input('Enter units used : ')
units = int(units)

if units <= 100  :
  w5perUnit = units*5
  print('Total water bill charges is',w5perUnit)
elif units <= 200 :
  w10perunit = units*10
  print('total water bill charges is',w10perunit)
elif units >= 250 :
  w20perunit = units*20
  print('total water bill charges is',w20perunit)
