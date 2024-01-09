def armstrong(n):
    num_digit=str(n)
    got_length=len(num_digit)
    
    armstrong = sum(int(digit) ** got_length for digit in num_digit)
    return armstrong==n

n=153
res=armstrong(n)
if res:
    print('armstrong')
else:
    print('not armstrong')