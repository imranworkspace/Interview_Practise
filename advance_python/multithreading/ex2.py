import threading
import time

def worker(n):
    print(f'stared {n} thread')
    time.sleep(1) # releasing thread
    print(f'finished {n} thread')
thread=[]


for i in range(1,6):
    t = threading.Thread(target=(worker),args=[i,])
    t.start()
    thread.append(t)

for t in thread:
    t.join()