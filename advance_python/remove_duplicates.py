# remove duplicates from single list 
lst=[1,2,3,4,3,2,3,4]
print(list(set(lst)))

# remove duplicates from two lists
list1 = [1,2,3]
list2 = [4,5,6,1,2,3]

print(set(list1) ^ set(list2))