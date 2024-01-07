def palindrome(name):
    rev = ''.join(reversed(name))
    if name==rev:
        return True
    else:
        return False

name=input('enter name : ')
res = palindrome(name)

if res:
    print(f'{name} is palindrome')
else:
    print('not palindrome')