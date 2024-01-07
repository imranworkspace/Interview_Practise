def decorator_fun(func,func2,x,y):
    def wrapper_fun():
        print('wrapperfun worked')
        print(x+y)
        return func(),func2()
    print('decorator fun worked')
    return wrapper_fun
def display():
    print('------------------')
    print('display fun worked')


def show():
    print('show fun worked')
decorator_show = decorator_fun(show,display,10,20)
decorator_show()

