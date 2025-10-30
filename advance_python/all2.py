my_array = [8, 12, 9,7, 2, 4, 11, 7]
minVal = my_array[0]
print(minVal)
for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

#  expected [1, 3, 5, 7, 9]
# expected [2,4,6,8]
lcomp = [i for i in range(1,11) if i & 1 == 0]
print(lcomp)

# reverse list by recursion
def r_lst(l):
    if len(l)==0:
        return []
    return [l[-1]] + r_lst(l[:-1])
    
l=[7,8,9]
print(r_lst(l))
# reverse list by recursion without re
def rev_2(l2):
    rev_lst_ex=[]
    if len(l2)==0:
        return []
    else:
        for element in l2:
            rev_lst_ex=[element]+rev_lst_ex
    return rev_lst_ex
l2=[4,5,6]
print(rev_2(l2))
# reverse str
def rev_str1(name):
    return name[::-1]
name="imran"
print(rev_str1(name))
# reverse str without slicing
def rev_str2(name2):
    r_str=''.join(reversed(name2))
    return r_str
name2="imran"
print(rev_str2(name2))
# reverse number 
def rev_num(n):
    rev_n=0
    while n>0:
        remainder = n%10
        rev_n=(rev_n*10)+remainder
        n=n//10
    return rev_n
n=321
print(rev_num(n))
# palindrom string,name
def pali(name3):
    if len(name3):
        return ''
    return name3==name[::-1]
name3="imran"
p = pali(name3)
if p:
    print(f'{name3} palindrom')
else:
    print(f'{name3} not palindrom')
    
# fibonaccie series
n=5
count,n1,n2=0,0,1
while count<n:
    print(n1)
    n1,n2=n2,n1+n2
    count+=1
# rev string withour reverse and recursion
def str_rev(name4):
    str_temp=''
    for s in name4:
        str_temp=s+str_temp
    return str_temp
name4="irfan"
print(str_rev(name4))

#armstrong
def arm(n):
    num_digit=str(n)
    len_digit=len(num_digit)
    arm=sum(int(digit) ** len_digit for digit in num_digit)
    if arm==n:
        print(f'{n} is armstrong number')
    else:
        print(f'{n} is not armstrong number')
        
n=153
arm(n)

for i in range(2,101):
    for j in range(2,101):
        if i%j==0:
            break
    if i==j:
        print(i)
# find second largest number 
lst5=[8,3,7,98,105,126]
lst5.sort()
print(lst5)
lst5.reverse()
print(lst5)
sorted_lst = sorted(lst5,reverse=True)
print(sorted_lst[1])

#####
def lst_to_dct(lst):
    d=dict()
    for key,item in enumerate(lst,start=200):
        if isinstance(item,list):
            d[key]=lst_to_dct(item)
        else:
            d[key]=item
    return d
lst = ['a','b',['e','f'],'g',['h']]
# expected from above list 
# dict = {0:'a',1:'b',2:{0:'e',1:'f'},3:'g',4:{0:'h'}}
print(lst_to_dct(lst))

# factorial 
def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))
n=5
from math import factorial
def fact2(n):
    if n==1:
        return 1
    return factorial(n)

def fact3(n):
    my_factorial=1
    while n>0:
        my_factorial=my_factorial*n
        n=n-1
    return my_factorial

print(f'fact of {n} is {fact(n)}')
print(f'fact of {n} is {fact2(n)}')
print(f'fact of {n} is {fact3(n)}')

def list_to_dict(new_list):
    d={}
    for key,value in new_list:
        if key not in new_list:
            d[key]=value
        else:
            d[key]=value
    return d

new_list = [(5, 'a'), (2, 'b'), (3, 'c'), (5, 'ab')]
# expected {5: 'ab', 2: 'b', 3: 'c'}
print(list_to_dict(new_list))



# find second largest number from given list 
lst=[1,2,3,5,6,7,8,9,0,12,34,56,78]
n = sorted(lst,reverse=True)
print(n[1])

# expected 56

########### regular expression example
passage="Amidst this tranquil scene, a lone figure emerged from the shadows, moving with silent determination. It was a young adventurer, his eyes alight with curiosity and his spirit fueled by the promise of discovery. With each step, he ventured deeper into the wilderness, drawn by the mysteries that lay hidden within its depths."
import re
pattern="his"
match_found = re.findall(pattern,passage)
print(match_found)
print(len(match_found))

## output : 
# ['his', 'his', 'his']
# 3

name="Imran@123"
d,s,a=0,0,0
for st in name:
    if st.isdigit():
        d+=1
    elif st.isalpha():
        a+=1
    else:
        s+=1
print(d,s,a)

print()
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
a,b,c=tuple1
print(a)
print(b)
print(c)

print()


#swap tuple
tupl1=(11,99)
tupl2=(88,44)
tupl2,tupl1=tupl1,tupl2
print(tupl2)
print(tupl1)
print()
# Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.difference_update(set2))
print()
print()

d = {1:'imran',2:'irfan'}
print(d.keys())
print(d.values())
print(d.items())
print(max(d.values()))
print(max(d.items()))
print()
print()

d2,d3,d4={},{},{}
d4=d
d2=d
d3=d.copy()

d2.pop(1)
print(d2)
print(d)

d4=d3.copy()
d4.pop(1)
print('d4')
print(d4)
print(d3)

d3.update({3:'muskan'})
print(d3)

d3.popitem()
print(d3)
