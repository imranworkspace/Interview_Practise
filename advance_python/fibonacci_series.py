n=int(input('enter no :-> '))
count,n1,n2=0,0,1
while count <=n:
    print(n1)

    temp=n1+n2
    n1=n2
    n2=temp
    count+=1
