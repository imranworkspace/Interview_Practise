# import numpy
from numpy import *

# std_roll = numpy.array([101,102,103,104,105])
# std_roll = array([101,102,103,104,105])
std_roll = array([101,102,103,104,105],dtype=float)# convert into float
print(std_roll)
print(std_roll.dtype)
print(std_roll[0])
print(std_roll[1])
print(std_roll[2])
print(std_roll[3])
print(std_roll[4])

for st in std_roll:
    print(st)

std_roll[2]=110
# std_roll[1]="imran" # not working 

print('use of while loop')
i=0
while i<len(std_roll):
    
    print(std_roll[i])
    i+=1

# creating array by linspace
print('linspace()') 
# rnum = linspace(1,8,num=5)
rnum = linspace(1,8,num=5,endpoint=False)
print(rnum)

# create array by logspace with base 10 bydefault
print('logspace()')
rnum2 = logspace(1,8,num=5,dtype=int)
print(rnum2)

# create array by arange()
print('arange()')
a=arange(1,10,2)# odd num
a2=arange(2,10,2)# odd num
print(a)
print(a2)

# create array using zeros function
print('zeros()')
z1=zeros(5)
z2=zeros(5,dtype=int)
print(z1)
print(z2)

print('ones()')
o1=ones(5)
o2=ones(5,dtype=int)
print(o1)
print(o2)

