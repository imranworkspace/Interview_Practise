# from multipledispatch import dispatch

# @dispatch(int,int)
# def myfun(a,b):
#     print(a*b)

# @dispatch(float,float,float)
# def myfun(a,b,c):
#     print(a*b*c)
# myfun(1,2)
# myfun(1.0,2.0,3.0)

import multiprocessing

def cube(a):
    print(a*a*a)
def sq(a):
    print(a*a)
    
p1=multiprocessing.Process(target=cube,args=(10,))
p2=multiprocessing.Process(target=sq,args=(10,))

p1.start()
p2.start()
p1.join()
p2.join()
print('done')
print('all done')