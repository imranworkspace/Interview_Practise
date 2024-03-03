
class Animal:
    def speak(self):
        print('animcal can speak')

class Dog(Animal):
    def speak(self):
        print('dog can speak')
a=Dog()
a.speak()