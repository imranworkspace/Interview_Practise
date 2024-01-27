from abc import ABC,abstractmethod

class Car(ABC):
    def milege(self):
        pass

class Tesla(Car):
    def milege(self):
        print('tesla milege 17 kmpl')

class Tata(Car):
    def milege(self):
        print('tata milege 14 kmpl')

class Hyundai(Car):
    def milege(self):
        print('hyundai milege 18 kmpl')

t = Tesla()
t.milege()

ta=Tata()
ta.milege()

h=Hyundai()
h.milege()

