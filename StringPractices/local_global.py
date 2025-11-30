a=50
def show():
    a=10
    print('local variable A : ',a)
  
show()
print('global variable A : ',a)


i=10
def accessglobal():
    global i # if any changes in local into global variable it will effect on glocal variable also
    i+=1
    print('in local',i)

print('-----')
print('access global variable using global keyword')

accessglobal()
print('global ',i)


j=11
def accessglobal2():
    j=9
    print('local variable A : ',j)
    globals()['j'] # if any changes in local into global variable it willnot effect on glocal variable also
    j=40
    print('global variable temp changed : ',j)

print('-----')
print('access global variable using globals()')
accessglobal2()
print('global variable not changed ',j)