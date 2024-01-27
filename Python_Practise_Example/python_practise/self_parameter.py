# The self parameter is reference to the currenct instance of the class, 
# and it is used to access variable that belongs to the class.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'your name is {self.name} and your age is {self.age}')

name=input('enter your name :-> ')
age=int(input('enter age :-> '))
p=Person(name,age)
p.show()
        