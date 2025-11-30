def decor1(num):
    def inner():
        a=num()
        add=a+10
        return add 
    return inner

def decor(num):
    def inner():
        b=num()
        multi= b * 10
        return multi
    return inner

@decor 
@decor1
def num():
    return 10

# num = decor(decor1(num))
print(num())