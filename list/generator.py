def gen(a,b):
    while a<=b:
        yield a
        a+=1
result = gen(1,5)
print(next(result))
print(next(result))
print('--')
for i in result:
    print(i)
