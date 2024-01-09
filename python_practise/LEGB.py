from math import pi
# pi=3.14
def enclosing():
    # pi=3.144
    def local():
        # pi=3.1444
        print(pi)
    local()
enclosing()
    