

def disp(sh):
    # print('disp function')
    return 'disp function' + sh()

def show():
    return ' show function'

print('pass function to another function')
r = disp(show)
print(r)
print('--------------------------------')

def disp2():
    def show2():
        print("show2 fun worked")

    print("disp fun worked")
    show2()
    print('rest of code ')


print('function calling inside function')
disp2()


print('--------------------------------')


