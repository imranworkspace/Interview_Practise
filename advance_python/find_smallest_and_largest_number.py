l=[1,2,3,4,1,2,3,4,5,7,8,9]
lset=set(l)
lset.remove(min(lset))
print(min(lset))