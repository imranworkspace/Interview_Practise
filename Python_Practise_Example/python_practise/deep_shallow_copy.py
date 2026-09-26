import copy 
l=[[1,2],[3,4]]
print(id(l))
dp=copy.deepcopy(l)
sp=copy.copy(l)
l[0][0]=45
print('dp',dp)
print(sp)
print(id(dp))
print(id(sp))