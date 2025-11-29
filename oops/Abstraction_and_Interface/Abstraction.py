from abc import ABC,abstractmethod

class Defence_System(ABC):
    @abstractmethod
    def gun(self):
        pass

    def show(self):
        print("concrete class")

class Navy(Defence_System):
    def gun(self):
        print('Navy Gun - AK47')
    

class Army(Defence_System):
    def gun(self):
        print('Army Gun - AK41')

class Airforce(Defence_System):
    def gun(self):
        print('Airforce Gun - AK40')

na=Navy()
na.gun()
na.show()
print()
arm = Army()
arm.gun()
arm.show()
print()
ar = Airforce()
ar.gun()
ar.show()