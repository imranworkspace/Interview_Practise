def prime2(a,b):
    return [n for n in range(a,b) 
            if n>1 and all([n%i!=0 for i in range(2,n//2+1)])]

print(prime2(1,100))


