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