################################
# create factorial examle using decorator who calculate function execution time
import time
def time_decor(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        end=time.time()
        es=end-start
        print(f'estimate time for {func.__name__}',es)
        return func
    return wrapper()

@time_decor
def fibo(n):
    count,n1,n2=0,0,1
    while count<n:
        print(n1)
        n1,n2=n1+n2,n1
        count+=1
n=5
fibo(n)

@time_decor
def fprime():
    for i in range(2,101):
        for j in range(2,101):
            if i%j==0:
                break
        if i==j:
            print(i)
fprime()
