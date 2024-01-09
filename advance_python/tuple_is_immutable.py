tp1=(1,2,3)
tp2=(7,8,9)
print(id(tp1))
print(id(tp2))

tp1=tp1+tp2
tp3=tp1
print('after tuple concatination ',tp1)
print(id(tp3))

print('-----------------------')
lst1=[1,2,3]
lst2=[7,8,9]
print(id(lst1))
print(id(lst2))

lst1.extend(lst2)
lst3=lst1
print('after list concatination : ',lst1)
print(id(lst3))