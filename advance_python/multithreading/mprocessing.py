from multiprocessing import Process
import time

def heavy_task():
    x=0
    for _ in range(50_000_000):
        x+=1

if __name__=="__main__":
    t1=time.perf_counter()
    p1 = Process(target=heavy_task)
    p2 = Process(target=heavy_task)
    
    p1.start()
    p2.start()
    p1.join()
    p1.join()
    t2=time.perf_counter()
    print(t2-t1)
    