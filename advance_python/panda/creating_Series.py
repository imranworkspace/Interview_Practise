# two ways using empty() using inputs using list,array,dict
import pandas as pd 
import numpy as np
x=pd.Series()
print(x)
print(type(x))

# second way using inputs array
y=np.array(['i','m','r','a','n'])
x=pd.Series(y)
print(x)
print(type(x))

# second way using inputs dictonary
d={1:"imran",2:'irfan'}
x=pd.Series(d)
print(x)
print(type(x))


# second way using scalar value
x = pd.Series(4,index=[1,2,3,4])
print(x)
print(type(x))

# access element
x = pd.Series([1,2,3],index=[1,2,3])
print(x)
print(type(x))
print(x[1])