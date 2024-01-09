try:
    10/0
except ZeroDivisionError as e:
    print('exception occured -> ',e)
else:
    print('no exception')
finally:
    print('always executed')