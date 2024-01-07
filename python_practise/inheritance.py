class P:
    def display(self):
        print('display fun called')
class B(P):
    def show(self):
        print('show fun called')
b=B()
b.display()
b.show()