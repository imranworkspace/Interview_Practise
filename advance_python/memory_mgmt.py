import sys

a=5
print(f'id a = 1st {id(a)}',sys.getrefcount(a))
b=a
print(f'id a = 2st {id(b)}',sys.getrefcount(a))
c=a
print(f'id a = 3rd {id(c)}',sys.getrefcount(a))
del b
print('after del b ',sys.getrefcount(a))
del c
print('after del c ',sys.getrefcount(a))