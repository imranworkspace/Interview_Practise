################################
# create factorial examle using decorator who calculate function execution time
import time
def time_decorator(func):
    def wrapper(*args,**kwargs):
        start_=time.time()
        end_=time.time()
        process_time = end_-start_
        print('execution time ',process_time)
        return func
    return wrapper()
    
@time_decorator
def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))
n=5
print(f'fact of {n} of {fact(n)}')

from math import factorial
@time_decorator
def fact2(n):
    return factorial(n)
n=5
print(fact2(n))

@time_decorator
def fibo(n):
    count,n1,n2=0,0,1
    while count<n:
        print(n1)
        temp=n1+n2
        n2=n1
        n1=temp
        count+=1
n=5
fibo(n)

n=5
print(f'fact of{n} is {fact(n)}')
