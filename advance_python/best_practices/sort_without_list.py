lst = [5, 2, 9, 1, 5, 6]
# print(len(lst))

for i in range(len(lst)): # 6
    for j in range(len(lst)-i-1): # 6-0-1= 5,
        if lst[j]>lst[j+1]:   # lst[j]=5, j pointing to memory location, 
                             # lst[j+1] 2,  = 5>2
            lst[j],lst[j+1]=lst[j+1],lst[j]
    print(lst)
    input()
    # 2,5,9,1,5,6 -0
    # 2,5,9,1,5,6 -1
    # 2,5,1,9,
print('result',lst)