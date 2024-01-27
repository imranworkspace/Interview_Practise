def decorator_fun(func):
    def wrapper_fun():
        print('wrapperfun worked')
        return func()
    print('decorator fun worked')
    return wrapper_fun

def show():
    print('show fun worked')
decorator_show = decorator_fun(show)
decorator_show()

@decorator_fun
def display():
    print('------------------')
    print('display fun worked')
display()