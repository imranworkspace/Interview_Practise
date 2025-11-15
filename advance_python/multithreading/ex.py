import time
import threading
from concurrent.futures import ThreadPoolExecutor
def func(n):
    print('func is calling waiting for {} seconds'.format(n))
    time.sleep(n) # releasing thread
    return n 
# -------------------
# Sequential version
# -------------------
time1=time.perf_counter()
func(10)
func(4)
func(2)
func(1)
time2=time.perf_counter()
print(time2-time1)
#--------------------------------------------------------
# -------------------
# Threading version
# -------------------
time1=time.perf_counter()
t1=threading.Thread(target=func,args=[10])
t2=threading.Thread(target=func,args=[4])
t3=threading.Thread(target=func,args=[2])
t4=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
time2=time.perf_counter()
print(time2-time1)
#--------------------------------------------------------
if __name__=="__main__":
    # -------------------
    # ThreadPoolExecutor version
    # -------------------
    time1=time.perf_counter()
    with ThreadPoolExecutor() as executor:
        # multiple files or urls download from internet or application I can do it using below with with ThreadPoolExecutor
        timer_lst =(10,4,2,1)
        for results in executor.map(func,timer_lst):
        # for result in results:
            print(results)
    time2=time.perf_counter()
    print(time2-time1)