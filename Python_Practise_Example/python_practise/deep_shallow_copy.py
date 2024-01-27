import copy
l=[[1,2],[3,4]]
dp=copy.deepcopy(l)
dp[0][0]=45    
print(dp)
print(l)

import copy
l=[[1,2],[3,4]]
sp=copy.copy(l)
sp[0][0]=45    
print(sp)
print(l)