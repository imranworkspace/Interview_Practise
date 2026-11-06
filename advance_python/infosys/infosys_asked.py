# decorator 
# try exception in detailed
# solid principal
    # 1.single responsibility principal - single class should handle only single responsibility like Generate report not printing it 
    # 2.open and closed principal - new functionality should added without changing existing code  
    # 3.Liskov Substitution Principal - Bird example with fly method  so Penguen also bird but it cannot fly so LSP here 
    # 4.Interface Segregation Principal - it should not force method it does not need.
    # 5.Dependencies Invertion Principal - depends on abstraction rather than concreate class ex.Payment service should
    # depends on paymentgateway not directly any specific gateway ex. paypal
# what is decent patterns
# interview asked have you implemented algorithm in your project? ex.searching sorting algorithm
    # हाँ, मैंने अपने project में algorithmic logic implement किया है।

    # उदाहरण के लिए, मेरे project में एक Product Search API थी, जहाँ user products को name और category के आधार पर search कर सकता था और price के आधार पर sort कर सकता था।

    # मैंने filtering के लिए list traversal का उपयोग किया और sorting के लिए Python का sorting algorithm use किया। Filtering की time complexity O(n) थी और sorting की complexity सामान्यतः O(n log n) होती है।

    # FastAPI में मैंने इन operations को एक GET API के through expose किया था। इसलिए frontend/API client query parameters जैसे category, keyword और sort_by_price भेज सकता था और backend processed result return करता था।

    # इससे मुझे algorithm को सिर्फ coding problem के रूप में नहीं, बल्कि real-world application में implement करने का experience मिला।
---------------------------------------------------------------------------------
# 1.project structure

    fastapi-project/
    │
    ├── main.py
    ├── models.py
    ├── schemas.py
    ├── services.py
    └── requirements.txt
---------------------------------------------------------------------------------
# 2.models.py 
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 60000},
    {"id": 2, "name": "Mouse", "category": "Electronics", "price": 800},
    {"id": 3, "name": "Keyboard", "category": "Electronics", "price": 1500},
    {"id": 4, "name": "Chair", "category": "Furniture", "price": 5000},
]
---------------------------------------------------------------------------------
# 3.shemas.py
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
---------------------------------------------------------------------------------
# 4.Algorithm — Search + Sorting
from models import products


def search_products(
    keyword: str | None = None,
    category: str | None = None,
    sort_by_price: bool = False
):
    result = products

    # Filtering algorithm
    if keyword:
        result = [
            product for product in result
            if keyword.lower() in product["name"].lower()
        ]

    if category:
        result = [
            product for product in result
            if product["category"].lower() == category.lower()
        ]

    # Sorting algorithm
    if sort_by_price:
        result = sorted(result, key=lambda x: x["price"])

    return result
---------------------------------------------------------------------------------
# 5. FastAPI Endpoint

from fastapi import FastAPI
from typing import Optional

from services import search_products

app = FastAPI()


@app.get("/products")
def get_products(
    keyword: Optional[str] = None,
    category: Optional[str] = None,
    sort_by_price: bool = False
):
    return search_products(
        keyword=keyword,
        category=category,
        sort_by_price=sort_by_price
    )
---------------------------------------------------------------------------------






import logging 
from functools import wraps

logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers= [
            logging.FileHandler("logging.log"),
            logging.StreamHandler()]
)

def loggin_decor(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            logging.info("started %s", func.__name__)
            r = func(*args,**kwargs)
            logging.info("finished %s %s",func.__name__,args)
            return r 
        except ZeroDivisionError:
            logging.exception(
                'cannot divided by zero'
                )
            return None
        except Exception as e:
            logging.exception(
                'exception occured %s '
                ,e)
            raise 
    return wrapper

@loggin_decor
def add(a,b):
    return a+b

@loggin_decor
def mul(a,b):
    return a*b

@loggin_decor
def div(a,b):
    return (a/b)

add(1,2)
mul(1,2) 
div(10,0) 


# find second highest salary 
lst=[
    {'name':'imran','salary':30000},
    {'name':'sohel','salary':45000},
    {'name':'kiran','salary':55000}
]
highest=second_higest=float('-inf')
for emp in lst:
    salary=emp['salary']
    if salary>highest:
        second_higest=highest
        highest=salary
    elif salary>second_higest:
        second_higest=salary
print(second_higest)

# Sort dictionary by value
salary_dict=[55000,5000,1000]
d2 = {num:i for i,num in enumerate(salary_dict)}
r = dict(sorted(d2.items(),key=lambda x: x[1],reverse=True))
print(r)



my_dict = {
    "apple": 50,
    "banana": 20,
    "mango": 40,
    "orange": 10
}

r = dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))
print(r)

# # solid principle
# # 1. single responsibility principle
# # one class should take care only one responsibility

# class Employee:
#     return only Employee details 

# class EmployeeReport
#     return only employee report basis on employee
#     details like empid,name,salary,age,desig 

# # 2. open/close principle
# we can add add more code without affecting
# existing code 

# class CreateUPIPayment:
#     pass 

# class PhonePayUpiPayment: # newly added no affect 
# # on existing code 
#     pass 

# # 3.Liskov Substituion principle
# we can create new code basis on existing code
# ex. duck typing - pengiun cannot fly -Throw and exception

# #4. Interface S.principle
# in other class it should not force to insert 
# existing method as per their need it should work

# from typing import Protocol
# class Printer(Protoco):
#     print('printer works')

# class Scanner(Protoco):
#     printer('scanner works')

# class Multi(Protoco)
#     def printer_fun():
#         print('printer works')
#     def scanner_fun():
#         print('scanner works')
# # 5. Dependency I principle
# high level business logic 
# it should be abstract no need to depends on each other

# class Order:
#     print('send order')

# class Notification:
#     print('send notification')