# staticmethod, instance method, class method 
class Person:
    name="imran"
    # static method 
    @staticmethod
    def work():
        print('work')
    # instance method 
    def show(self):
        print('show fun call')
    @classmethod
    def disp(cls):
        print(f'you name is {cls.name}')
p=Person()
p.work()
p.show()
p.disp()