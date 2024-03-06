import concurrent.futures
import time

def myfun(n):
    print('function stop for {}'.format(n))
    time.sleep(n)
    return n
# s=time.perf_counter()
# myfun(2)
# myfun(4)
# myfun(3)
# myfun(10)
# e=time.perf_counter()
# print(e-s)

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        s=time.perf_counter()
        time_lst=[2,4,3,10]
        results = executor.map(myfun,time_lst)
        for r in results:
            print(r)
        e=time.perf_counter()
        print(e-s)
