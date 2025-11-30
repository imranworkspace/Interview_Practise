def decor(fun):
    def inner():
        a = fun()
        result = a+20
        return result
    return inner
@decor
def num():
    return 10

# inner_fun = decor(num)
# print(inner_fun())
print(num())