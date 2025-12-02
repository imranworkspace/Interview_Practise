class Student(object):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def get_name(self): # accessor method type of instance method
        print(f'your name is {self.name}')        
    
    def get_roll(self):
        print(f'your roll no is {self.roll}')  # accessor method type of instance method  

    def set_roll(self,r): # mutator method type of instance method
        self.roll = r
        print(f'updated roll no is {self.roll}')      

s=Student("Zunaisha",200)
s.get_name()
s.get_roll()
s.set_roll(100)