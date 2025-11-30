# ex;1
lst=[1,2,3,[4,5]]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3][0])
print(lst[3][1])
print()
lst[3][0]=40

for l in lst:
    print(l)

print('same example but 2nd')
# ex;2
b=[[4,5]]
lst=[1,2,3,b]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print('-----')
print('2d list')
a =[[1,2,3],[4,5,6]]

print("a[0] : ",a[0])
print("a[1] : ",a[1])
print('-----')
print('old element : ',a[1][2])
a[1][2]=500
print('new element : ',a[1][2])
print('-----')



print('without index')
for i in range(len(a)):
    print('row index : ',i)
    for j in range(len(a[i])):
        print(j)
    print()

print('without index - 2')
for i in a:
    for j in i:
        print(j)
    print()

input()
print('with index')
for i in range(len(a)):
    for j in range(len(a[i])):
        print('i',i,'-',j,'=',a[i][j])
    print()

input()
print('with index - while loop')
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print('i',i,'-',j,'=',a[i][j])
        j+=1
    i+=1
    print()