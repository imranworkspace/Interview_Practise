class Student(object):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def disp(self):
        print(f'your name is {self.name} and your roll no is {self.roll}')        

class User(object):
    @staticmethod # static method - access other class attributes and methods
    def show(std):
        print(f'User Class student name {std.name} and roll is {std.roll}')
        std.disp()

std = Student("Imran",121)

User.show(std)