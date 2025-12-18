def rev_number(n):
    rev_number=0
    while n>0:
        remainder = n%10
        rev_number=(rev_number*10)+remainder
        n=n//10
    return rev_number

n=1002
print(rev_number(n))
######################################################################
# palindrom number 
# rev number
def rev(n):
    rev_number = 0
    while n>0:
        remainder = n%10
        rev_number=(rev_number*10)+remainder
        n=n//10
    return rev_number
    
n=121
res = rev(n)

if n==res:
    print(f'{n} is palindrome')
else:
    print('not palindrome')


# reverse list
def rev_lst(lst):
    if len(lst)==0:
        return []
    return [lst[-1]] + rev_lst(lst[:-1])
lst=[1,2,3,2,1]
result = rev_lst(lst)
if lst==result:
    print('Yes given list is palindrome ',lst)
else:
    print('No given list is palindrome ',lst)