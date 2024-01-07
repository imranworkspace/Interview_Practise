def bre():
    for i in range(1,10):
        if i==5:
            print('---')
            break
        print(i)

def conti():
    for i in range(1,10):
        if i==5:
            print('---')
            continue
        print(i)
def pa():
    for i in range(1,10):
        if i==5:
            print('pass stmt')
            pass
            print('after pass')
bre()
conti()
pa()