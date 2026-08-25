lst=[3,2,1]
lst.append(4)
lst.extend((10,20,4))
lst.extend([30,40])
lst.extend({6,7}) # 3,2,1,4,10,20,4,30,40,6,7
print(lst)
lst.remove(4)# 4 will remove from first occurance and # 3,2,1,10,20,4,30,40,6,7
lst.insert(4,1000)# 3,2,1,10,1000,20,4,30,40,6,7
lst.pop()## 3,2,1,10,1000,20,4,30,40,6
print('pop',lst)
print(lst)
print('----')
lst.pop(2)## 3,2,1,10,1000,20,4,30,40,6
print('pop',lst)
input()
lst.sort()#
print(lst)
lst.sort(reverse=True)#
print(lst)
print(lst.index(1000))

#copy lst 
lst2,lst3=[],[]
lst2.extend(lst)
lst3=lst2
print('lst2',lst2)
print('lst3',lst3)


lst.clear()
print(lst)
