from abc import ABC,abstractmethod

class Defence_System(ABC):
    @abstractmethod
    def gun(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Navy(Defence_System):
    def gun(self):
        print('Navy Gun - AK47')
    def area(self):
        print('Worked on water')

class Army(Defence_System):
    def gun(self):
        print('Army Gun - AK41')
    def area(self):
        print('Worked on land')

class Airforce(Defence_System):
    def gun(self):
        print('Airforce Gun - AK40')
    def area(self):
        print('Worked on air')

na=Navy()
na.gun()
na.area()
print()
ar = Army()
ar.gun()
ar.area()
print()
ar = Airforce()
ar.gun()
ar.area()