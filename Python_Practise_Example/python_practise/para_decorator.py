def decorator_fun(func):
    def wrapper_fun(*args, **kwargs):
        print('wrapper fun worked')
        add = kwargs.get('x', 0) + kwargs.get('y', 0)
        print(add)
        return func(*args, **kwargs)

    print('decorator fun worked')
    return wrapper_fun

def show():
    print('show fun worked')
    print('--------------')

# Using the decorator without @ syntax
decorator_show = decorator_fun(show)
decorator_show()

@decorator_fun
def display(x,y):
    print('disp fun worked')

# You can pass additional arguments to the decorator using keyword arguments
display(x=1, y=2)
