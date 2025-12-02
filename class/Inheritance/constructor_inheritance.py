class Father:
    def __init__(self):
        print('father class constructor')
    
    def show(self):
        print('fahter show')
class Child(Father):
    def disp(self):
        print('child disp')

c=Child()
