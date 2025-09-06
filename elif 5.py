#Athor = Saksham Joshi
#Date = 4th of Semptember 2025
#description = working with if and else commands 
is_raining = input('is it raining outside : ').lower()
user_windy = input('is it windy outside : ').lower()

if is_raining == ('yes') and user_windy == ('no') :
  print('carry an umbrella')
elif is_raining == ('yes') and user_windy == ('yes') :
  print('too windy to carry an umbrella')

else :
  print('have a good day')
  

