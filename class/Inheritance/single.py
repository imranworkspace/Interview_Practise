class P(object):
    money = 1000
    def home(self):
        print('home')
    
    def business(self):
        print('business')

    def car(self):
        print('car')
    
    @classmethod
    def salary(cls):
        print("father hourly salary",cls.money)

class C(P):
    def job(self):
        print('job-software engg')
    def bmw(self):
        print('son owe bmw car')

c=C()
c.home()
c.business()
c.car()
c.job()
c.bmw()
c.salary()