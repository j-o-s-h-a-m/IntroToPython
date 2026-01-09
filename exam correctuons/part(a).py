cardNum = input('Welcome to CardCheck. Enter your card number: ')
cardNumInt = int(cardNum) #567
while cardNumInt > 9:
    cardNumInt  = cardNumInt//10 #5

if cardNumInt == 7 :
    print('This is a ZincCard')
elif cardNumInt == 8 :
    print('This is a WincCard')
    
cardNumlen = len(cardNum)
print(cardNumlen)

    

    


        
        
        
        

    
    


