def leap_year(year):
    if year%400==0:
        print('this is leap year')
    elif year%4==0 and year%100!=0:
        print('this is leap year')
    else:
        print('not leap year')
leap_year(2004)
# find repleated numbers from list
lst=[12,3,4,5,6,7,8,1,2,3,4,5,6,3,4,3,5,6,7,8,8]
d={}
nlst=[]
for i in lst:
    if lst.count(i)>1 and i not in nlst:
        d[i]=lst.count(i)
print(d)
print(nlst)
print()
# expected my name is imran
l1=['my','is']
l2=['name','imran']
r=[x+' '+y for x,y in zip(l1,l2)]
mystr=''
for s in r:
    mystr=mystr+s+' '
    
print(mystr)

lst=["heart","earth", "act","tac","cat","rahul","imran",
"stones","tones","god","dog"]
nlst=[]
for i in range(len(lst)-1):

    if sorted(lst[i])==sorted(lst[i+1]):
        nlst.append((lst[i],lst[i+1]))
print(nlst)

# sort lst without sort
lst = [1,2,3,1,2,4]
for i in range(len(lst)):#5
    for j in range(len(lst)-i-1):#3
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

print()

''' Find duplicates in a list '''
lst2 = [1,2,3,1,2,4]
nlst=[]
for n in lst2:
    if n not in nlst:
        nlst.append(n)
print(nlst)
print()
def lst_to_dct(lst):
    d={}
    for k,v in enumerate(lst,start=0):
        if isinstance(v,list):
            d[k]=v 
        else:
            d[k]=v 
    print(d)
    
lst = ['a','b',['e','f'],'g',['h']]
# expected from above list 
# dict = {0:'a',1:'b',2:{0:'e',1:'f'},3:'g',4:{0:'h'}}
lst_to_dct(lst)


def rev_num(num):
    rev=0 
    while num>0:
        rev = rev*10 + num%10 
        num//=10
    return rev 
print(rev_num(121))

print()

my_array = [8, 12, 9,7, 2, 4, 11, 7]
minV=maxV=my_array[0]
for n in my_array:
    if minV>n:
        minV=n 
    if maxV<n:
        maxV=n 
print('max',maxV)
print('min',minV)
my_array.sort()
print(my_array)
my_array.reverse()
print(my_array)
import time 
def decor_main(func):
    def wrapper(*args):
        s = time.perf_counter()
        r=func()
        e = time.perf_counter()
        print(f'time taken for {func.__name__} - {e-s}')
        return r 
    return wrapper

@decor_main
def show():
    time.sleep(0.1)

show()
print()

# prime 
def prime(a,b):
    for n in range(a,b):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break 
            print(n,end=' ')
prime(1,101)
print()

# fibonacci
n=10 
a,b=0,1 
count=0 
while n>count:
    print(a)
    a,b=b,a+b 
    count+=1 

# fact 
def fact(n):
    if n==1:
        return 1 
    return n*fact(n-1)
print(fact(5))
print()

from math import factorial 
print(factorial(5))
print('fact---')
print()
# rev list, string using recursion
def rv_str(name):
    return name==name[::-1]

def rv_str2(name):
    rev_ = ''.join(reversed(name))
    return rev_==name

def rv_str3(name):
    nstr=''
    for s in name:
        nstr=s+nstr
    return name==nstr
    
name="irfan"
print(rv_str(name))
print(rv_str2(name))
print(rv_str3(name))



def rv_lst(lst):
    if len(lst)==0:
        return []
    return [lst[-1]] + rv_lst(lst[:-1])

l=[4,3,2,1]
print(l[::-1])
print(rv_lst(l))
rev_l=[]
for i in l:
    rev_l=[i]+rev_l
print(rev_l)
nlst=[]
for i in reversed(l):
    nlst.append(i)
print(nlst)


# list operation 
l=[3,2]
l.append([4,5,6])
l.extend((7,8,9,4,5))
print(l)
print(l.index(4))
l.pop()
print(l)
l.remove(4)
print('remove ',l)
# l2=l.sort()
# print(l2)
# string operations 
s=' imran '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print('case')
print(s.lower())
print(s.upper())
print(s.title())
print('replace')
print(s.replace("mr","rf"))
print('bool')
print(s.startswith("i"))
print(s.endswith("i"))
print(s.isdigit())
print(s.isalpha())
