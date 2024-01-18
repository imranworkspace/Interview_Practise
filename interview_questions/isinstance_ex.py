# isinstance () method call when if we want to check
# belongs to object of class is same or not 

#syntax:-> isinstance(object,class_Name)

n=5
print(isinstance(n,int)) # true
print(isinstance(n,float)) # true


print('-----------------------')
class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'my name is {self.name}')
p = Person("imran")
p.show()
print(isinstance(p,Person))