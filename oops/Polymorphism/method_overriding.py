class Dog:
    def speak(self):
        print('dog say bhaww')
class Cat(Dog):
    def speak(self):
        super().speak()
        print('cat say meawwwwwww')
c=Cat()
c.speak()