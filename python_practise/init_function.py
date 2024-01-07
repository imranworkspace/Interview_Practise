class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print(f'hi {self.name}')
name = float(input('enter your name :-> '))
p=Person(name)
p.say_hi()        