from numpy import *
a=array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print('0th row all columns')
r = a[0,:]
print(r)
print('1th row all columns')
r = a[1,:]
print(r)
print('2th row all columns')
r = a[2,:]
print(r)

input()
print('0th columns all rows')
r = a[:,0]
print(r)
print('1th columns all rows')
r = a[:,1]
print(r)
print('2th columns all rows')
r = a[:,2]
print(r)

print('----------------------')
print('10th')
r=a[0:1,0:1] # start row 0:col 0,  row 0 col 0 =10
print(r)

print('90th')
r=a[2:3,2:3]
print(r)

input()
print('----------------------')
print('range()')
print('select 0,1th row, column should be 1,2')
r=a[0:2,1:3]
print(r)