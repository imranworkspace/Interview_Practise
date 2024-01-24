def decor_fun(func):
    def wrapper_fun(a, b):
        add = a + b
        print(add)
        return func()

    print('main fun called')
    return wrapper_fun

def show():
    print('show fun called')

decor_show = decor_fun(show)
decor_show(20, 30)
print()

@decor_fun
def display():
    print('display fun called')

display(20, 30)
