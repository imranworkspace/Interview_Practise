from numpy import *

mobile_rows=int(input('enter total rows : '))# 3
age_cols=int(input('enter total cols : '))# 2
mob_age = zeros((mobile_rows,age_cols),dtype=int)
print(mob_age)
n=len(mob_age)

print('for loop - with indexing')
# using for loop with indexing
for row in range(n):# starting from 0 row
    for col in range(len(mob_age[row])): # total element of row 0
        col_val = int(input('enter value : '))
        mob_age[row][col] = col_val
print(mob_age)

# using while loop with indexing
print('while loop - with indexing')
i=0
n=len(mob_age)

while i<n:#0<3
    j=0 
    while j < len(mob_age[i]):# 0 < 
        x = int(input("enter value : "))
        mob_age[i][j]=x
        j+=1
    i+=1
    print()
print(mob_age)