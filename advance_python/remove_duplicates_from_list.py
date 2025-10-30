lst=[6,3,3,5,6,7,4,1,7,9,2,33,44,55,100]
print(list(set(lst)))

# witout using set
list1 = [1, 2, 3, 2, 4, 4, 5, 6, 6]
l_unique = []
for l in list1:
    if l not in l_unique:
        l_unique.append(l)

for l in lst:
    if l not in l_unique:
        l.append(l)

print(l_unique)

