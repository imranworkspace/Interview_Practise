from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def milege(self):
        pass
    
    def car_info(self):
        print('cars have 4 wheels ')

class Tesla(Car):
    def milege(self):
        print('tesla provide 14 kmpl')

class Tata(Car):
    def milege(self):
        print('tata provide 18 kmpl')

te = Tesla()
ta = Tata()

te.milege()
te.car_info()
print()
ta.milege()
ta.car_info()
