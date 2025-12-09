# count prime numbers from 1 to 101

# prime numbers # 2,3,5,7.11
def prime(a,b):
    for n in range(a,b):
        if n>1:
            for i in range(2,n//2+1): # range(2,7)    # 2,3,4,5,6
                if n%i==0:
                    # print('not prime ')
                    break
            else:
                
                print(f'no is prime {n}')

prime(1,100)