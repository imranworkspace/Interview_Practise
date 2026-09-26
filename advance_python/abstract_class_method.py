

import time
s=time.perf_counter()

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def milege(self):
        pass 
    def wheels(self):
        print('each car have 4 wheels')

class Tata(Car):
    def milege(self):
        print('tata give 19 kmpl milege')
class Hyn(Car):
    def milege(self):
        print('hundai give 22 kmpl milege')
ta=Tata()
h=Hyn()
ta.milege()
h.milege()


def prime(a,b):
    time.sleep(2)
    for n in range(a,b):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break 
            else:
                print(n,end=' ')

# sort without sort()
def sort_without(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    print(lst)

def pali(name):
    time.sleep(1)
    print(name[::-1])
    n=len(name)
    s=name
    return all(s[i]==s[n-i-1] for i in range(n))
    
def minmax(myarray):
    time.sleep(2)
    minV=maxV= myarray[0]
    for i in myarray:
        if minV>i:
            minV=i 
        if maxV<i:
            maxV=i 
    print('min value',minV)
    print('max value',maxV)

myarray=[9,4,6,3,1,23,45]

def fibo(n):
    time.sleep(2)
    count,a,b=0,0,1
    while count<=n:
        print(a,end=' ')
        a,b=b,a+b 
        count+=1 

def enagram(lst):
    time.sleep(1)
    nlst=[]
    for i in range(len(lst)-1):
        if sorted(lst[i])==sorted(lst[i+1]):
            nlst.append((lst[i],lst[i+1]))
    print(nlst)
    
def call_by_ref(lst):
    time.sleep(1)
    lst.append(10)
    print('before call by ref',lst)

def call_by_val(a):
    time.sleep(1)
    a+=10
    print('before call by val ',a)
    
lst=["heart","earth", "act","tac","cat","rahul","imran",
"stones","tones","god","dog"]
lst3=[2,3]
print('before call by ref',lst3)
call_by_ref(lst3)
enagram(lst)
fibo(5)
print(pali('imran'))
prime(1,100)
lst2 = [5, 2, 9, 1, 5, 6]
sort_without(lst2)
minmax(myarray)
a=10
print('before call by val ',a)
call_by_val(a)

e=time.perf_counter()
print(f'time req {e-s:.2f}')


from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def milege(self):
        pass
    
    def car_info(self):
        print('cars have 4 wheels ')

class Tesla(Car):
    def milege(self):
        print('tesla provide 14 kmpl')

class Tata(Car):
    def milege(self):
        print('tata provide 18 kmpl')

te = Tesla()
ta = Tata()

te.milege()
te.car_info()
print()
ta.milege()
ta.car_info()
