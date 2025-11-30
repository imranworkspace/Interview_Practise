import sys
print('### default : get recursion limit ',sys.getrecursionlimit())
print('### set recursion limit ',sys.setrecursionlimit(150))
print('### get recursion limit ',sys.getrecursionlimit())



i=0
def myfun():
    global i 
    # i=0 # local variable not work here
    i+=1
    print('imran : ',i)
    myfun()
myfun()

