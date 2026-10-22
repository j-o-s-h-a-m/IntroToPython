some_dict = {}
print(some_dict)
some_dict2 = dict()
print(some_dict2)

some_dict = {"key":"value","fruit":"apple"}
print(some_dict)

#list of tuples
list_of_tuples =[("key","value"),("fruit","apple")]
#convert list to dictionary
some_dict2 = dict(list_of_tuples)
print(some_dict2)
#add new item to the dictionary 
some_dict2["price"] = 2.03
#change fruit to orange
some_dict2["fruit"] = "orange"
print(some_dict2)
some_dict2["dictionary"]={"a":1,"b":2,"c":3}
print(some_dict2)

#list keys in dictionary
for key,values in some_dict2.items():
    print(values,"-->",values)
#delete item from dictionary
'del some_dict2' # will delete the entire disctionary
del some_dict2["fruit"]
print(some_dict2)
#check if item in dictionary
if "fruit" in some_dict2:
    print("fruit is still present - failed delete")
else:
    print("fruit removed")
new_dict = {"a":5, "b":4 , "c":7}
print(new_dict.items())
def sf(x):
    return x[1]
tuple_sorted_dict = sorted(new_dict.items(),key=sf,reverse = True)
print(tuple_sorted_dict)
print(dict(tuple_sorted_dict))

#tuple_sorted_dict = sorted(new_dict.items(),key = sf)


