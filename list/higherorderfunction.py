marks=[40,20,10,60,70,20,90]
def high_score(n):
    if n>60:
        return True
print(id(marks))
result = list(filter(high_score,marks))
print(result)
print(id(result))

fruits = ['apple','apriot','banana']
mobj = list(map(lambda a:a[0]=='a',fruits))
print(mobj)

from functools import reduce

lst=[1,2,3,4,5]
res = reduce(lambda a,b:a+b,lst)
print('total ',res)