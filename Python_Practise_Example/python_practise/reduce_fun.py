from functools import reduce
mylst=[1,2,3,4,5]
addition_using_reduce_fun = reduce(lambda x,y:x+y,mylst)
print('total : ',addition_using_reduce_fun)

fruits = ['apple','banana','apriot','kiwi']
filtered_list  = list(filter(lambda s:s[0]=='a',fruits))
print(filtered_list)

map_list = list(map(lambda s:s[0]=='a',fruits))
print(map_list)