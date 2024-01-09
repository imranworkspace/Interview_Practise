class A:
    def abc(self):
        print('a')
class B(A):
    def abc(self):
        print('b')
class C(A):
    def abc(self):
        print('c')
class D(C,B):
    pass
d=D()
d.abc()
