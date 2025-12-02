class Mobile(object): # object is base class for Mobile class
    fp="Yes" # class variable , fp - IS CLASS NAMESPACE  here
    def __init__(self,m): # self -> have memory address of object and internally passed to object
        self.model=m # instance variable, m - IS INSTANCE NAMESPACE here
    
    def show(self): # instance method
        print('model : ',self.model) # accessing instance variable

    # classmethod decorator used to access class variable
    @classmethod
    def fp_access(cls): # class method - cls is variable like self
        print(cls.fp) # access class variable

    @staticmethod
    def staticm(m,p,cls):
        model=m
        price=p
        print(f"model name is {model} and price is {price}")

realme = Mobile("Realme Pro") # realme object is also INSTANCE NAMESPACE here
realme.show() # accessing instance method

realme.fp_access() # accessing class method

realme.staticm("Realme 2",1000) # accessing static method
