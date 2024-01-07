def sqrt(n):
    print('n',n)
    for i in range(1,n+1):
        yield i*i

a=sqrt(9)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))