# INFOSYS ASKED
# typhinting
    # Type hinting means specifying the expected data type of variables, function parameters, and return values. It helps with readability, IDE autocomplete, static checking, and maintaining large projects.
    # Python does not enforce type hints at runtime by default.
def getEmployees()->list[str]:
    return ['imran','afreen',20]
print(getEmployees())

def getEmployee(name:str)->str:
    return f'Hello {name)}!'
print(getEmployee("imran"))


def getSalary(salary:float)->float:
    print(type(salary))
    print(salary)
getSalary(5000.0)

def getAdd(a:int,b:int)->int:
    print(type(a+b))
    print(a+b)
getAdd(1,2)

def getEmpl(name:str,age:int)->dict[str,int|str]:
    return {
        "name":name,
        "age":age
    }
name=input('enter your good name : ')
age=int(input(f'enter your age {name} : '))
print(getEmpl(name,age))
---------------------------
l=[1,2,3,5,4,5,2,3,1,3,5]

# using lambda function use reduce to find the sum 
from functools import reduce

total_ = reduce(lambda x,y:x+y,l)
print(total_)

# find new list contains count of duplicates
d=dict()
nlst=[]
for k in l:
     if l.count(k)>1 and k not in nlst:
         nlst.append(k)
         d[k]=l.count(k) 
    
print(nlst)
print(d)
         

# decorator for time takes to sample function
import time 
def decor_main(func):
    def wrapper():
        s=time.perf_counter()
        r = func()
        e=time.perf_counter()
        print(e-s)
        return r 
    return wrapper
    
@decor_main
def sample():
    time.sleep(3)
    print('sample fun called')

# sample()


nums = [2,7,11,15,3,6]
target = 20
res = []

for i in range(len(nums)):
    seen = {}
    for j in range(i + 1, len(nums)):
        need = target - nums[i] - nums[j]
        if need in seen:
            res.append([i, seen[need], j])
        seen[nums[j]] = j

print(res)


s = "a,bc$d"

s = s[::-1]
s = s.replace(",", "#").replace("$", ",").replace("#", "$")

print(s)