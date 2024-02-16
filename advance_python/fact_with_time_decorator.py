################################
# create factorial examle using decorator who calculate function execution time
import time
def time_decoreator(func):
    def wrapper_fun(*args,**kwargs):
        print('inside wrapper')
        start=time.time()
        end=time.time()
        excution_time = end-start
        print('excution_time ',excution_time)
        return func
    return wrapper_fun
  
@time_decoreator    
def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))

n=5
print(f'fact of{n} is {fact(n)}')
