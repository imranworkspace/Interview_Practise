class Father(object):
    def showF(self):
        print("Father") 
class Mother(object):
    def showM(self):
        print("Mother")
class Son(Father,Mother):
    def showS(self):
        print("Son")

s=Son()
s.showS()
s.showF()
s.showM()