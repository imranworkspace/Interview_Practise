# Company ASked
'''

1. 4 golder achievments 
	My 4 key achievements are:

	1. Developed scalable backend APIs using Python, Flask, Django, and FastAPI.
	2. Improved application performance and reliability through optimization and monitoring.
	3. Implemented CI/CD and deployment using Docker, AWS, and Jenkins.
	4. Successfully delivered projects while meeting business and technical requirements.

2. my kubernetes cluster goes 95% up then how can I deal with it 
3. some power outages happnes during production as a backend developer or infrastructure developer what steps we gonna do instead of ALB 
4. which aws services for maintaining environment variables 
5. jenkins structure 
6. kubernetes structure
7. learn more detailed in prometheous and graphana
8. file system handling it goes incresed day by day then how can I deal with it 
9. in jenkins 404 happnes we got from end users/client on production then what steps we gonna do 
10. instead of JWT which authentication and authorization services you used?

'''

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

# typehinting fastapi 
from fastapi import FastAPI

app = FastAPI()

@app.get("/employee/{employee_id}")
def get_employee(employee_id: int) -> dict:
    return {
        "id": employee_id,
        "name": "Imran"
    }


# typehinting sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class Employee:
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
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