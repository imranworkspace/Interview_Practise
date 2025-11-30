def add(a,b): # a,b formal argument
    c=a+b
    return c
print(add(1,2)) # actual argunment

# Types of arguments
'''
1.positional argument
2.keyword argument
3.Default argument
4.Variable Length argument
5.Keyword Variable Length argument
'''

'''1.positional argument'''
def pw(x,y):
    return x**y 

r = pw(2,5)# 2 position arument passing - correct way
# r = pw(2,5,3)# 3 position arument passing - incorrect way
print(r)


'''2.keyword argument'''
def show(name,age):
    return f"your name is {name} and age is {age}"

# r=show(name="imran",age=30)
r=show(age=30,name="imran") # doesnt matter it will give us correct output, but no of argumnet must be same 
# r=show(age=30,name="imran",roll=121) # incorrect way 
print(r)

'''3.Default argument'''
def show2(name,age=33): # here age is default value with age=33;
    return f"your name is {name} and age is {age}"

# r=show(name="imran",age=30)
r=show2(name="imran") # doesnt matter it will give us correct output, but no of argumnet must be same 
# r=show2(age=30,name="imran",roll=121) # incorrect way 
print(r)


'''4.Variable Length argument'''
def sumv(*nums):
    total=0
    for i in nums:
        total+=i
    print('total ',total)

sumv(1,2,3,4,5) # we can pass no of arguments 


'''5.Keyword Variable Length argument'''
def kv(**dict):
    print(dict)

kv(a=1,b=2)

print('------------------Lamda--------------------')
x=5
addi = lambda x,y:x+y
print(addi(2,5))
print('--------')
fruits=['apple','apriot','mango']
f = list(filter(lambda a:a[0]=='a',fruits))
print(f)
print('--------')

add_sum_mul = lambda a,b:(
    a+b,
    a-b,
    a*b)
add_,sub,mul = add_sum_mul(2,3)
print('addition : ',add_)
print('subtraction : ',sub)
print('multiplication : ',mul)

'''default argument'''
additi = lambda a,b=10:a+b
print(additi(5))

'''Nested lambda function'''
add = lambda x=10 : lambda y:x+y
result=add()
print('Nested ex: lambda',result(20))

'''passing lambda function to another function'''

def show(a):
    return a(8)

r = show(lambda x:x+x)
print(r)

'''return lambda function by function'''
def add2():
    x=5
    return lambda y:x+y

a = add2()
print(a(30))

'''Immediate Involked Function Expression [IIFE]'''
print((lambda a,b:a+b)(1,2))