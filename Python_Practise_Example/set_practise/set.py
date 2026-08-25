# months = {'imran'}
myset = set([8,9,10,11,12,1,2,3,4,5,6,7])    
# discard() not raised any error if item is avaialble or not
myset.discard(100)
print(myset)   

# remove() raised an error if item is avaialble or not 
# raised an error KeyError: 'January'
# myset.remove(100)
# print(myset)

myset.add(100)
print(myset)

myset2=set()
myset3=set()

myset2=myset
print('myset2',myset2)

myset3=myset.copy()
print('myset3',myset3)

myset.pop()
print('pop',myset)

myset.remove(2)# 2 remove from set 
print('pop',myset)

