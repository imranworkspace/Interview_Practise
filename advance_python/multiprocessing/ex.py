from multiprocessing import Process
import time

def count(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':

    start = time.time()

    p1 = Process(target=count, args=(10**7,))
    p2 = Process(target=count, args=(10**7,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Multiprocessing time:", time.time() - start)
