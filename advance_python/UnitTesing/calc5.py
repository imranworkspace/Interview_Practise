def add(a,b):
    return a+b

def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                print(False,f'{n} is not prime number')
                break
        else:
            return True

def 