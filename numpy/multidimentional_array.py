from numpy import *

names_nikname=array([
    ['imran','afreen','zunaisha'],
    ["immu","nakti","zunnu"]
    ],dtype=str)
print(names_nikname[0][0],names_nikname[1][0])
print('-----')
# modify
names_nikname[0][0]="imran"
names_nikname[1][0]="bittu"
print(names_nikname)
print(names_nikname.dtype)
print('-----')
# access element using for loop
print('for loop - without index')
for row in names_nikname:
    print('row no ',row)
    for c in row:
        print(c)
    print('')
print('-----')

# access element using for loop
print('for loop + inner loop - with index')
n=len(names_nikname)
print(n)
print('-----')
for i in range(n):# 0,1 -> rows
    for j in range(len(names_nikname[i])): #names_nikname[0] -> columns 
        print(names_nikname[i][j]) # names_nikname[0][0],names_nikname[0][1],names_nikname[0][2]

print('-----')
# access element using while loop
print('while loop')
print()
n=len(names_nikname)
i=0
while i<n:
    j=0
    while j<len(names_nikname[i]):
        print(names_nikname[i][j])
        j+=1
    i+=1
    print()


mobile_rows=int(input('enter total rows : '))# 3
age_cols=int(input('enter total cols : '))# 2
mob_age = zeros((mobile_rows,age_cols),dtype=int)
print(mob_age)
n=len(mob_age)
print('----')
print('inner loop - without index')

for r in mob_age:
    for c in r:
        print(c)
    print()
print('----')
print('inner loop - with index')
for row in range(n):# n=5,row=0
    for col in range(len(mob_age[row])): # mob_age(0)
        print(mob_age[row][col])
    print()


