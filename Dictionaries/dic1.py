# user_inp = input("enter a sentence : ")
# user_inpt = user_inp.split()
f = open('book.txt','r')
f = f.read()
# f = f.lower()
f_inpt = f.split()

print(f)
a = 0
dic = {}
while a == 0:
    print('enter 1 if u want to calculate frequecy of each word in your sentence')
    print('Press 2 to calcualte word on the book')

    input_user = input('Enter Your option : ')
    if input_user == '1' :
        dic = {}
        for i in user_inpt:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i] = 1
        a = 1
    if input_user == '2' :
        dic = {}
        for i in f_inpt:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i] = 1
        a = 1    
    else:
        a = 1
    input_user = ''
    
print(dic['the'])

# val_dic = {}
# count = 0 
# for i in dic:
#     for j in dic:
#         if j == i:
#             count += 1
#         val_dic[j] = count
#         count = 0
# print(val_dic)
            
            
