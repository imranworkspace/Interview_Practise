import multiprocessing

def print_sqr(n):
    print(f'squareroot of {n}')

def print_cube(n):
    print(f'cube of {n}')

if __name__=='__main__':
    p1=multiprocessing.Process(target=print_sqr,args=(50,))
    p2=multiprocessing.Process(target=print_cube,args=(50,))

    p1.start()
    p2.start()

    #wait until process is completed
    p1.join()
    p2.join()

    print('done!!!')