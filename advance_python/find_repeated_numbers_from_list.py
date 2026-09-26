# find repleated numbers from list
lst=[12,3,4,5,6,7,8,1,2,3,4,5,6,3,4,3,5,6,7,8,8]
d=dict()
for item in lst:
    if item in d:
        d[item]+=1
    else:
        d[item]=1
for k,v in d.items():
    print(k,':',v)

lst2=[12,3,4,5,6,7,8,1,2,3,4,5,6,3,4,3,5,6,7,8,8]

# using list
repleated=[]
for v in lst:
    if lst.count(v)>1 and v not in repleated:
        repleated.append(v)
print(repleated)

# using dictionary 
count={}
for num in lst2:
    count[num]=count.get(num,0)+1 
for k,v in count.items():
    print(k,' - ',v)