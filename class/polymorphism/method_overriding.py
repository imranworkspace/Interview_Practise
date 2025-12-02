class Add(object):
    def result(self,x,y):
        print(f'Addition {x+y}')
class Multi(Add):
    def result(self,a,b):
        super().result(10,20)
        print(f'multiplication {a*b}')

m=Multi()
m.result(10,20)