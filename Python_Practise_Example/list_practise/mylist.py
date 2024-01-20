lst=[1,2,3]
print(len(lst))
print(type(lst))
print(tuple(lst))
lst.append(4)
print(lst)

mytup = (4,5,6,7,8)
print(type(mytup))
lst2=[9,8,7]
lst.extend(mytup)
lst.extend(lst2)
print(set(lst))

print('copy lst')
lst3=[0,0,0,0]
lst3.extend(lst)
print(lst3)


print('remove item ')
lst3.pop()
print(lst3)

lst3.remove(4)
print(lst3)

lst3.clear()
print(lst3)

mytup2 = tuple(lst)
print(type(mytup2))
print(len(mytup2))






