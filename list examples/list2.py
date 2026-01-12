lst = [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,17,18,19,20]
val = [17,23,18,19]
print("The List is : ",val)
while True:
    print("main menu")
    print("1.Insert")
    print("2.delete")
    print("3.exit")
    ch = int(input("Enter your choice 1/2/3 : "))
    if ch == 1 :
        item = int(input("Enter item:"))
        pos = int(input("Insert at which position?"))
        index = pos - 1
        val.insert(index,item)
        print('success! list now is : ',val)
    elif ch == 2:
        print(" deletion Menu")
        print("1.delete using value")
        print("2.Delete using index")
        print("3.Delete a sublist")
    dch = int (input("Enter choice(1 or 2 or 3): "))
    if dch == 1 :
        item = int(input("enter item to be deleted : "))
        val.remove(item)
        print("list now is :",val)
    elif dch == 2:
        index = int(input("Enter item to be deleted : "))
        val.pop(index)
        print("List now is : ",val)
    elif dch == 3 :
            l = int (input("enter lower limit of list slice to be deleted: "))
            h = int(input("enter upper limit of list slice to be deleted: "))
            del val[l:h]
            print("List now is : ",val)
    else:
            print("valid choices are 1/2/3 only ")
            
        
    
            
            

