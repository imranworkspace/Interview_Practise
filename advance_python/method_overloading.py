# best example of method overloading
def add(a, b, c=0):
    return a + b + c

print(add(1, 2))
print(add(1, 2, 3))


'''from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    return a+b

@dispatch(int,float)
def add(a,b):
    print('int,float')
    return a+b


@dispatch(float,float)
def add(a,b):
    return a+b

@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c

@dispatch(float,float,float,float)
def add(a,b,c,d):
    return a+b+c+d

print(add(10,10.0))'''




# from multipledispatch import dispatch

# @dispatch(int,int)
# def myfun(a,b):
#     print(a*b)

# @dispatch(int,int,int)
# def myfun(a,b,c):
#     print(a*b*c)

# @dispatch(float,float,float)
# def myfun(a,b,c):
#     print(a*b*c)
# myfun(1,2)
# myfun(1.0,2.0,3.0)
# myfun(1,2,3)

# import multiprocessing

# def cube(a):
#     print(a*a*a)
# def sq(a):
#     print(a*a)
    
# p1=multiprocessing.Process(target=cube,args=(10,))
# p2=multiprocessing.Process(target=sq,args=(10,))

# p1.start()
# p2.start()
# p1.join()
# p2.join()
# print('done')
# print('all done')

