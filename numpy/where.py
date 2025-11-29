from numpy import *

a=array([101,2,103,104])
b=array([1,4,3,400])
result = where(a>b, a, b)
print(result)


print('nonzero()')
a2=array([101,0,103,104,0])
result=nonzero(a2)
print(result)

print('aliasing()')
a3=array(['imran','irfan','afreen','zunnu'])
b3=a3
print(id(a3))
print(id(b3))

# memory location diffrent but if we changes in a or b then affect into both array
print('view()')
demo=array([1,2,3])
temp = demo.view()
demo[1]=50
print(demo)
print(temp)

# memory location diffrent but if we changes in a or b then affect not in anoter one
print('copy()') 
demo_copy=array([1,2,3])
temp_copy = demo_copy.copy()
demo_copy[1]=50
print(demo_copy)
print(temp_copy)
