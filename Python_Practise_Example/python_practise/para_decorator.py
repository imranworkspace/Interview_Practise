import time
def main(func):
    def wrapper(t):
        s=time.perf_counter()
        time.sleep(t)
        print(f'{func.__name__} worked')
        e=time.perf_counter()
        print(e-s)
        return func()
    return wrapper

@main
def show():
    pass
show(2)

@main
def disp():
    pass
disp(3)
