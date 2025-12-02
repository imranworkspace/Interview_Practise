class Mobile(object): # object is base class for Mobile class
    def __init__(self): # self -> have memory address of object and internally passed to object
        self.model='Realme x' # instance variable
    
    def show(self): # instance method
        print('model : ',self.model) # accessing instance variable

realme = Mobile() # creating object for it , object have memory location of realme object
realme.show() # access class method using object or instance

