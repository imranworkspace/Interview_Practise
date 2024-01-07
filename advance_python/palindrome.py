def palindrome(name):
    return name==name[::-1]
name=input('enter name ')
res=palindrome(name)
if res:
    print(f'{name} is palindrome')
else:
    print('not palindrome')