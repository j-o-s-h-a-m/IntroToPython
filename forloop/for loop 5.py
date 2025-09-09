#Author = Saksham Joshi
#9/8/2025
#for loops
total = 0

for number in range(5) :
    user_number = input('Enter Your Number : ')
    user_number = int(user_number)
    add_to_total = input('Add to total? : ').lower()
    if add_to_total == 'yes' :
        total = total + user_number
        print(total)
        
    
    

    

