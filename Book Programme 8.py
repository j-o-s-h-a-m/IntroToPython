user_height = input('Enter Your height in cm: ')
user_height = int(user_height)
user_height_in_foot = user_height/30.48
user_height_in_inches = ((user_height_in_foot)-int(user_height_in_foot))*12
print('Yourheight is',int(user_height_in_foot),'ft',int(user_height_in_inches),'in')