class GrandFather(object):
    def showGF(self):
        print('Grandfather')
class Father(GrandFather):
    def showF(self):
        print('Father')
class Son(Father):
    def showS(self):
        print('Son')

s = Son()
s.showGF()
s.showF()
s.showS()