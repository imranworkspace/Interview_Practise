from numpy import *
n=int(input("Enter no of element : "))
a = zeros(n,dtype=int)
# for loop using zeros()
for i in range(n):
    el=int(input("enter element no : "))
    a[i]=el
print(a)


n2=int(input("Enter no of element : "))
a2 = ones(n2,dtype=int)
# while loop using
i=0
while(n2>i):
    el2=int(input("enter no : "))
    a2[i]=el2
    i+=1
print(a2)