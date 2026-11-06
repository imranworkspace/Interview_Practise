


''''mostly asked 
introduction yourself 
VIMP -> why migration required only in python,when you done migration from .net project or C# project into fastapi which challeges you faced.
1.generator and iterator - more explain in details
2.decorator with example  - 
3.shallow and deep copy - explain it properly 
4.oops 4 pillars - defination and example
5.methods example - instance method,class method,static method 
6.type hinting
7.why async 
8.diff multithreading and multiprocessing and GIL 
9.diff between list and tuple 
10.context manager with and example - custom contextmanager 
11.what is pickle and its types
12.how memory managed in python 
13.coding - reverse string,reverse list,get common records from two list without for loop,
anagram 
14.design principle - must answers with examples
15.what is idempotency for payment gateway example and how to deal with regarding payment success
or not 
16.  file system handling it goes incresed day by day then how can I deal with it 
17. in jenkins 404 happnes we got from end users/client on production then what steps we gonna do 
18. instead of JWT which authentication and authorization services you used? 
19. fastapi middleware , use multiple middlewares then how it is executed top-bottom or bottom-top 
20. what is router and use of it.
21. unittest and pytest.
22. lambda funtion - map,filter and reduce
23. sort list without sort method in python 
24. set operation functions and use cases
25. nums = [2,7,11,15,3,6] target = 20
26. what is use of pydantic models in fastapi 

sql - 
 group by
 self table 
 2nd or third highest salary 
 diff between in and between 
 what is unique,primary,foreign key and composite key

k8s
my kubernetes cluster goes 95% up then how can I deal with it 
some power outages happnes during production as a backend developer or infrastructure developer what steps we gonna do instead of ALB  
1. schenario based questions regarding pod failed, crashbackoff,oomkilled error.
2. if my application working on local but failed in production.
3. my application working in production but suddenly request goes up and stop application responding
how will you track it solve it 
4. explain 4 golder offers 
6. what is RED and use - RATE,ERROR,   -Utility,S-how much resource taking load,E- 
7. what is elastic search and opensearch with and realtime example and indexing,documents related
8. kubernetes structure
9. 

djangot 
1.middleware and custom middleware
2.mixing 
3.routers 
4.authentication and authorization
5.what is 0Auth,Auth2 
6.serialization
7


aws
which aws services for maintaining environment variables

 ''''



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

extra:
* self join
* findout 2nd highest salary from emp where 2nd highest salary for users are same now using dense_rank()
* mixin, throttle,jwt

'''

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Registration
password = "MySecret@123"
print('your password ',password)

hashed_password = hash_password(password)

print("Store this in hashed DB:",hash_password)


# Login
login_password = "MySecret@123"

if verify_password(login_password, hashed_password):
    print(login_password,' - ',hash_password)
    print("Login successful")
else:
    print("Invalid username or password")

print('---------------------------------------')

# INFOSYS ASKED
# typhinting
    # Type hinting means specifying the expected data type of variables, function parameters, and return values. It helps with readability, IDE autocomplete, static checking, and maintaining large projects.
    # Python does not enforce type hints at runtime by default.
def getEmployees()->list[str]:
    return ['imran','afreen',20]
print(getEmployees())

def getEmployee(name:str)->str:
    return f'Hello {name}!'
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
# name=input('enter your good name : ')
# age=int(input(f'enter your age {name} : '))
# print(getEmpl(name,age))

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
#---------------------------
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
        print(f'{func.__name__} \t{e-s:.2f}')
        return r 
    return wrapper
    
@decor_main
def sample():
    time.sleep(3)
    print('sample fun called')

sample()


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


#pytest