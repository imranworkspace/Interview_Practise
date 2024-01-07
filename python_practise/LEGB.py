from math import pi
pi='global'
def enclose():
    pi='enclose'
    def local():
        pi='local'
        print(pi)
    local()
enclose()