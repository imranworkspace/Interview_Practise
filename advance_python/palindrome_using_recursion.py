def pali(name):
    if len(name)==1:
        return name
    elif name[0]==name[-1]: # compare first and last character
        return pali(name[1:-1]) # compare substring
    else:
        return False

name='madam'
res=pali(name)
if res:
    print('palindrome')
else:
    print('not palindrome')