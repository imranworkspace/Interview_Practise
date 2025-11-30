'''
* * * * *
* * * * *
* * * * *
* * * * *
'''
n = int(input('enter number for patter : '))
for i in range(n): # 0,1,2 and so on upto 4
    for j in range(n): # col
        print('$',end=' ')
    print()

'''
* 
* * 
* * * 
* * * *
* * * * *
'''
n = int(input('enter number for patter : '))
for i in range(n): # 0,1,2 and so on upto 4
    for j in range(i+1): # # 0,1,2 and so on upto 4
        print('*',end=' ')
    print()

'''
* * * * *
* * * *
* * * 
* *
*  
'''
n = int(input('enter number for patter : '))
for i in range(n): # 0,1,2 and so on upto 4
    for j in range(i,n): # # 0,1,2 and so on upto 4
        print('*',end=' ')
    print()

'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

n = int(input('enter number for patter : '))
for i in range(n): # 0,1,2 and so on upto 4
    for j in range(i,n): # # 0,1,2 and so on upto 4
        print('',end='')
    for j in range(i+1):
        print('*',end=' ')
    print()
