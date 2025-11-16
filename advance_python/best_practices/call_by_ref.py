# The function receives the reference (address) of the original value.
# Any change inside the function affects the original.

def call_by_Val(lst):
    lst.append(10)
    print('inside function',lst)

lst=[1,2]
call_by_Val(lst)
print('outside fun',lst)

# Python: Uses “call by object reference” — mutables behave like reference, immutables behave like value.