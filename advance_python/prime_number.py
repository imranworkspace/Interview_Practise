# count prime numbers from 1 to 101

def prime():
    for i in range(2,102):
        for j in range(2,102):
            if i%j==0:
                break
        if i==j:
            print(i,end=',')
print(prime())