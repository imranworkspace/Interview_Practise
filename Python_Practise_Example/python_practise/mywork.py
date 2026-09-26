import threading
import time

semaphore = threading.Semaphore(3)

def task(number):
    with semaphore:
        print(f"Thread {number} started")
        time.sleep(2)
        print(f"Thread {number} finished")

threads = [
    threading.Thread(target=task, args=(i,))
    for i in range(10)
]

for t in threads:
    t.start()

for t in threads:
    t.join()


import copy
l=[[1,2],[3,4]]
dp=copy.deepcopy(l)
sp=copy.copy(l)
l[0][0]=45    
print(dp)
print(sp)
print(l)



def my_middleware(get_response):
    print('one time init')
    
    def myfunc(request):
        print('before view called')
        resp = get_response(request)
        print('before view called')
        return resp 
    return myfunc



def fact(n):
    if n==1:
        return 1 
    else:
        return (n*fact(n-1))

print(fact(6))

def pali(name):
    r = ''.join(reversed(name))
    if name==r:
        print('palindrome')
    else:
        print('not palindrome')
pali('madam')



lst=[
    [1,2,'python'],
    [3,4,'is','good',5],
    ['language',5,7]
    ]

r=[lst[0][2],lst[1][2],lst[1][3],lst[2][0]]
mystr=''
for i in r:
    mystr=mystr+i+' '
print(mystr)

# expected my name is imran
l1=['my','is']
l2=['name','imran']

result = [x+' '+y for x,y in zip(l1,l2)]
mystr=''
for i in result:
    mystr=mystr+i+' '
print(mystr)


def pali(name):
    if len(name)==1:
        return name 
    elif name[0]==name[-1]:
        
        return name[1:-1]
    else:
        return False 

# r = pali('nitin')
# if r:
#     print('palindrome')
# else:
#     print('not palindrome')




def decor_main(func):
    def wrapper(*args,**kwargs):
          
        print('wrapper fun called')
        return func(*args,**kwargs)
    print('decor main fun called')
    return wrapper

# @decor_main
def show(name,age):
    print('show fun called')

# show(name="imran",age=33)

s = "a,bc$d"

s=s[::-1]
s=s.replace(",","#").replace("$",",").replace("#","$")
# print(s)


def sum_of_digit(n):
    total=0
    for i in str(n):
        total+=int(i)
    return total
# 
n=123456
# print(sum_of_digit(n))
# stateful 
class Stateful:
    def __init__(self):
        self.count=0 
    def count_fun(self):
        self.count+=1 
        return self.count 
s=Stateful()


def list_to_dict2(lst):
    d={}
    for index,val in enumerate(lst,start=0):
        if isinstance(index,list):
            d[index]=val 
        else:
            d[index]=val 
    print(d)
    print(type(d))

lst = ['a','b',['e','f'],'g',['h']]
# print(type(lst))
# list_to_dict2(lst)
# expected from above list 
# dict = {0:'a',1:'b',2:{0:'e',1:'f'},3:'g',4:{0:'h'}}


def list_to_dict(new_list):
    d={}
    for k,v in new_list:
        if k not in new_list:
            d[k]=v
        else:
            d[k]=v
    print(d)
        
# new_list = [(5, 'a'), (2, 'b'), (3, 'c')]
new_list = [(5, 'a'), (2, 'b'), (3, 'c'), (5, 'ab')]
# print(list_to_dict(new_list))
# {5: 'ab', 2: 'b', 3: 'c'}


# fibo 

def fibo():
    n=5
    a,b=0,1
    count=0
    while count<=5:
        print(a)
        a,b=b,a+b 
        count+=1 

# fibo()

def recur(lst):
    if not lst:
        return []
    return [lst[-1]] + recur(lst[:-1])

# print(recur([1,2,3]))
        
# 

