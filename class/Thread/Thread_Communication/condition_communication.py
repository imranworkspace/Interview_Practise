from threading import Thread, Condition
from time import sleep
# Condition is thread safe (maintaining automatic lock)
# method = notify(),notify_all() and wait()

'''
Use Condition → when waiting for a specific state
(e.g., wait until count > 0 before consuming)

'''


lst = []
def produce():
    cv.acquire() # lock by condition object
    print('prod acquires')
    for i in range(1,6): 
        lst.append(i)
        sleep(1)
        print('Product Produced',i)
    print()
    print('not yet notified')
    cv.notify()  # notify for one thread, notify_all() for multiple thread
    sleep(5)
    print("prod notified")
    cv.release()
    print("prod released")

def consume():
    cv.acquire() # lock it 
    print('con acquires')
    print('con wait for notify..')
    cv.wait(timeout=0) # wait for 0 sec
    print('wait over..')
    cv.release()
    print("con released")
    print(lst)

cv=Condition()
t1=Thread(target=produce)
t2=Thread(target=consume)

t1.start()
t2.start()