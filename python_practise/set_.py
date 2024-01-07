myset={'a','b','c','d','a'}
print(type(myset))
print(myset)

myset2=myset.copy()
myset2.add('f')
# myset2.clear()
print(myset2)

uni = myset.union(myset2)
print('uni',uni)

inter = myset.intersection(myset2)
print('inter ',inter)

diff = myset.difference_update(myset2)
print('diff',diff)