class Father:
    def __init__(self):
        print('father class constructor')
    
    def show(self):
        print('fahter show')
class Child(Father):
    def __init__(self):
        super().__init__() # overriding parent class constructor
        print('Child class constructor')
    def disp(self):
        print('child disp')

c=Child()  
