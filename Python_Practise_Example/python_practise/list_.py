lst2=[1,2]
lst=[1,2,2,7,3,4,5]
# lst.sort()
# lst.reverse()
# lst.append('p')
# lst.extend(['e','q'])
lst[0]='z'
lst[1]=10
print(lst)

lst.pop(0)
print(lst)
print(max(lst))
print(min(lst))

print(lst.count(2))
print(lst[2:])
print(sum(lst))