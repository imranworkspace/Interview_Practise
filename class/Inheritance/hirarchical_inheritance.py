class Father(object):
    def showF(self):
        print('father')
class Imran(Father):
    def showI(self):
        print('Imran')
class Muskan(Father):
    def showM(self):
        print('Muskan')

m=Muskan()
m.showF()
m.showM()
print('----')
i=Imran()
i.showF()
i.showI()