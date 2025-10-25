# palindrome with slicing  - DONE
def pali(name):
    return name==name[::-1]
name='madam'
res_got=pali(name)
if res_got:
    print(f'{name} is palindrome')
else:
    print(f'not palindrome')
    
# palindrome without slicing - DONE
def pali2(name):
    rev_sl = ''.join(reversed(name))
    return rev_sl==name

name='nitin'
res_got=pali2(name)
if res_got:
    print(f'{name} is palindrome')
else:
    print(f'not palindrome')

# fibonacci series - DONE
def fibo(n,count,n1,n2):
    while count<n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1
        
n=6
count,n1,n2=0,0,1
fibo(n,count,n1,n2)


# factorial with recursion- DONE
def fact_rec(n):
    if n==1:
        return 1
    return (n*fact_rec(n-1))
n=6
print(f'fact of {n} is {fact_rec(n)}')

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

from math import factorial
def fact2(n):
    if n==1:
        return 1
    else:
        return factorial(n)
        
n=5
result = fact(n)
result2 = fact2(n)
print(f'fact of {n} is {result}')
print(f'fact of {n} is {result2}')

# reverse list using inbluilt function - DONE
def rev(lst):
    rev_lst=[]
    if len(lst)==0:
        return []
    else:
        for element in reversed(lst):
            rev_lst.append(element)
        print(rev_lst)

lst=[1,2,3]
rev(lst)


# reverse list using recursion - DONE
def rev(lst):
    if len(lst)==0:
        return []
    else:
        return [lst[-1]] + rev(lst[:-1])
        
lst=[1,2,3]
print(rev(lst))

# reverse list without recursion - DONE


# armstrong number - DONE
def armstrong(n):
    num_str=str(n)
    num_digit=len(num_str)
    armstrong_num = sum(int(digit) ** num_digit for digit in num_str)
    return armstrong_num==n
n=int(input('enter number :- > '))
res=armstrong(n)
if res:
    print(f'{n} is armstrong')
else:
    print(f'{n} is not armstrong')
# prime number from 1 to 100
def prime():
    for i in range(2,101):
        for j in range(2,101):
            if i%j==0:
                break
        if i==j:
            print(i,end=',')
print(prime())

################################
# create factorial examle using decorator who calculate function execution time
import time
def time_decoreator(func):
    def wrapper_fun(*args,**kwargs):
        print('inside wrapper')
        start=time.time()
        end=time.time()
        excution_time = end-start
        print('excution_time ',excution_time)
        return func
    return wrapper_fun
  
@time_decoreator    
def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))

n=5
print(f'fact of{n} is {fact(n)}')




