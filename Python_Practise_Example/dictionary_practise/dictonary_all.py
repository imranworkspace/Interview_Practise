# create dictionary using dict() built in fun


# with dict() method   
# d = dict()

# Creating an empty Dictionary       
# d = {1:'imran',2:'irfan'}
d=dict()
print(d)
print(type(d))

# Creating a Dictionary       
# with each item as a Pair       
dummy =dict([(4, 'Rinku'), (2, 'Singh')])
print(type(dummy))
print(dummy[2])


# Accessing the dictionary values
Employee = {"Name": "Dev", "Age": 20, "salary":45000.0,"Company":"WIPRO"}      
print('Name %s '%Employee['Name'])
print('Age %d '%Employee['Age'])
print('Age %d '%Employee['salary'])


mydict=dict()
print(mydict)
print(type(mydict))

mydict[0]='imran'
mydict[1]='irfan'
mydict[2]='muskan'
mydict[4]=(30,27,24)
print(mydict)
print(type(mydict))

# get function
print('get() by passing key to fun ')
print('get item ',mydict.get(1))       
# Updating existing Key's Value       
print(mydict)
print(type(mydict))

# delete item and dictionary using del keyword

del mydict[0]
print(mydict)

# del mydict
# print(mydict)
# delete item and dictionary using pop() keyword

mydict.pop(2)
print(mydict)

# dictionary iteration using keys, values, items with x and x,y values
print('-------keys-----------')
for x in mydict.keys():
    print('keys',x)
print('-------values-----------')
for x in mydict.values():
    print('values',x)
print('--------items with x y -----------')
for k,v in mydict.items():
    print(k,' ',)
print('-------------------')

# extract dict data to tuple add into list then again convert
    # into another list
print('--------items only-----------')
new_dict = dict()
new_lst = list()
for x in mydict.items():
    print('items',x)
    new_lst.append(x)
print(dict(new_lst))

print('------get keys without key()------------')
for keys in mydict:
    print(keys)


print('------get keys without values()------------')

print('get values without using values()') 
print('1 using for loop')    
for keys in mydict:
    values = mydict[keys]
    print(values)

print(' Method 2: Using list comprehension')
values_obj = {key for key in mydict}
print(values_obj)

print('------------------------')
print('use built in fuction')

print('len ',len(mydict))
print('type ',type(mydict))

print('update method')
mydict.update({1:'myupdate'})
mydict.update({0:'mysorted'})
print('sorted method')
print(sorted(mydict))
print('------------------------')

mydict2 = mydict.copy()
print('new copy created using copy() ')
print(mydict2)

mydict2.clear()
print('clear dictionary using clear() ')
print(mydict2)

print('del dictionary using del keyword ')
del mydict2
# print(mydict2)

print()
print()
print('------------------------')
print('dictionary conversion into list')
list_of_tuples = list(mydict.items())
print('list_of_tuples ',list_of_tuples)
for kv in list_of_tuples:
    print(kv)
    
list_of_keys = list(mydict.keys())
print('list_of_keys ',list_of_keys)

list_of_values = list(mydict.values())
print('list_of_values ',list_of_values)

print()
print()
print('---------popitem---------------')
mydict.update({5:'afreen'})
print(mydict)

print('---------popitem performed---------------')
mydict.popitem()
print('removed lastest inserted item from dictionary by popitem() without any arguments')
print(mydict)
