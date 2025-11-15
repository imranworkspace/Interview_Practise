def add(a,b):
    return a+b 

def divide(a,b):
    if b==0:
        ValueError("zero division error")
    return a/b

def even(n):
    return n%2==0