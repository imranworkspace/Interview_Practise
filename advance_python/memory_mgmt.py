def fun2(p):
    q=p+10
    return q
    
def fun1(x):
    z=x+5
    p=fun2(z)
    return p

x=5
y=fun1(x)
print(y)


# stack   pri heap
# x          5
# y     
# fun1->
# z           10
# p   
# fun2->
# q    .      20

# output x=5 and y=20  z p (garbej collector also called dead object)


x1=5
y1=x1

z1=5

print(id(x1))
print(id(y1))
print(id(z1))
140714882316856
140714882316856
140714882316856