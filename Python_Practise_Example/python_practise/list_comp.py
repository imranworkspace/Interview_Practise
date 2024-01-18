# common way
l=[]
for i in range(10):
    if i%2==0:
        l.append(i)
print(l)

l=[i for i in range(10) if i%2==0]
print(l)