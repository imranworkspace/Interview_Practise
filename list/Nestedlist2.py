from numpy import *
print('with indexing - for loop')
print()
a=[1,2,3,[4,5]]
n=len(a)
for i in range(n): # 0,1,2,3
    if type(a[i]) is list: # a[3] is list type
        temp = len(a[i]) # 2=2
        for j in range(temp): # 0
            print(i,j,a[i][j])# a[3][0]=4,a[3][1]=5
    else:
        print(i,a[i]) # integer value will show 1,2,3

print()
print('with indexing - while loop')

n=len(a)
i=0
while i<n:# 0<3
    if type(a[i]) is list: # list is list =[True] or [False]
        temp = len(a[i]) # 2=2
        j=0
        for j in range(temp): # 0 in 2 
            print(i,j,a[i][j])# 3,0,a[3][0]=4,a[3][1]=5
            j+=1
    else:
        print(i,a[i]) # 0  a[0]=1,
                      # 1  a[1]=2,
    i+=1              # 2  a[2]=3

