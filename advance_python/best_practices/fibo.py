def fibo(n):
    fib=[0,1]
    [fib.append(fib[-1]+fib[-2]) for _ in range(2,n)]
    return fib
print(fibo(10))