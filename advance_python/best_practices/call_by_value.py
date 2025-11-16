'''
Definition
A copy of the actual value is passed to the function.
Key Point
Changes inside the function do NOT affect the original variable.
Works for primitive/immutable types.
'''

def callbyref(a):
    a+=1
    print('inside function ',a)

a=1
callbyref(a)
print('outside ',a)

