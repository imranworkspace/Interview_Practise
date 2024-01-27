def reverse_by_recursion(n):
    rev_number =0 
    while n>0:
        remainder=n%10
        rev_number=(rev_number*10)+remainder
        n=n//10
    return rev_number



n=1232
print(reverse_by_recursion(n))