
def fact(n):
    my_factorial=1
    while n>0:
        my_factorial=my_factorial*n
        n=n-1
    return my_factorial
num=7
print(f'fact of {num} is {fact(num)}')

# using built in function
from math import factorial
def fact(n):
    return factorial(n)

str=input('here for factorial we are using built in function so ENTER')    
n=int(input('enter factorial number '))
print(f'fact of {n} is {fact(n)}')