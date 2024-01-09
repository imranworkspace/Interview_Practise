
def fact(n):
    my_factorial=1
    while n>0:
        my_factorial=my_factorial*n
        n=n-1
    return my_factorial
num=7
print(f'fact of {num} is {fact(num)}')