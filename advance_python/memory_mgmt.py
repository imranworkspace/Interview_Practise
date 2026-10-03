import sys

lst=[1,]
print(sys.getrefcount(lst))
a=lst 
b=lst 
c=lst
print('total count - ',sys.getrefcount(lst))
del c 
del a
print('delete now count is  - ',sys.getrefcount(lst))