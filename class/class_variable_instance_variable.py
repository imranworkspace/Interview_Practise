class Mobile(object): # object is base class for Mobile class
    fp="Yes" # class variable
    def __init__(self): # self -> have memory address of object and internally passed to object
        self.model='Realme x' # instance variable
    
    def show(self): # instance method
        print('model : ',self.model) # accessing instance variable

    # classmethod decorator used to access class variable
    @classmethod
    def fp_access(cls): # class method - cls is variable like self
        print(cls.fp) # access class variable

print('before ')
realme = Mobile() # creating object for it , object have memory location of realme object
realme.show() # access class method using object or instance
realme.fp_access()

redmi = Mobile()
redmi.show()
redmi.fp_access

Mobile.fp="No" # change the class variable, once change this changes is done for rest of objects

print('------')
print('after modify class name ')
realme = Mobile() # creating object for it , object have memory location of realme object
realme.show() # access class method using object or instance
realme.fp_access()

redmi = Mobile()
redmi.show()
redmi.fp_access