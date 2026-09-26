################################
# create factorial examle using decorator who calculate function execution time
import time
def time_decor(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        
        try:
            tot = args[0]+args[1]
            print(tot)
        except (IndexError,TypeError) as e:
            pass 

        end=time.time()
        es=end-start
        print(f'estimate time for {func.__name__}',es)
        return func
    return wrapper()

@time_decor
def add():
    print('add called')

add(3,4)

@time_decor
def fprime():
    for i in range(2,101):
        for j in range(2,101):
            if i%j==0:
                break
        if i==j:
            print(i)
fprime()
