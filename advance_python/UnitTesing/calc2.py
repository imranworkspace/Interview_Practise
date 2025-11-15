def add(a,b):
    return a+b

def divide(a,b):
    if b==0:
        raise ValueError("zero cannot divide")
    return a/b

def evend(n):
    return n%2==0
