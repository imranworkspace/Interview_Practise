class Duck:
    def swim(self):
        print('I am duck I can swim')
class Fish:
    def swim(self):
        print('I am fish I can swim')
class Crocodile:
    def swim_walk(self):
        print('I am crocodile I can swim and walk as well')

def duck_typing(animal):
    animal.swim()

duck_typing(Duck())
duck_typing(Fish())
duck_typing(Crocodile())