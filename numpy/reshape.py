from numpy import *

a=array([1,2,3,4,5,6])
print('1 D array :\n\t',a)
twod=reshape(a,(2,3)) # array,rows,cols
print('2 D array :\n',twod)

print('-----')

a2=array([1,2,3,4,5,6,7,8,9,10,11,12])
threeD = reshape(a2,(2,3,2)) # 2 rows,3 cols, div 2 
print('three dimention\n',threeD)

'''threeDto_1D = reshape(threeD,12)
print('3d to 1d\n',threeDto_1D)
'''
# [optional] use flatten() to 2d,3d to 1d 
oneD = threeD.flatten()
print('3d to 1d\n',oneD)
