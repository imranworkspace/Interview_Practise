import sys

lst=[1,]
print(sys.getrefcount(lst))
a=lst 
b=lst 
c=lst
print('5 - ',sys.getrefcount(lst))
del c 
del a
print(sys.getrefcount(lst))