from threading import Thread, current_thread, Semaphore,Lock
from datetime import time
class Flight:
    def __init__(self,available_seats):
        self.available_seats=available_seats
        # self.lock = Lock()
        self.lock = Semaphore(2)
    
    def reservation(self,need_seats):
        self.lock.acquire()
        # with self.lock:
        print(f'available seats  are {self.available_seats}')
        name = current_thread().name 
        if self.available_seats >= need_seats:
            print(f'seats available to {name} - {need_seats}')
            self.available_seats -= need_seats
        else:
            print(f'no seats available {name} for you can book another flight')
        print()
        time(10)
        self.lock.release()

f = Flight(10)
t1 = Thread(target=f.reservation,args=(1,),name="imran")
t2 = Thread(target=f.reservation,args=(2,),name="vicky")
t3 = Thread(target=f.reservation,args=(3,),name="sonu")
t4 = Thread(target=f.reservation,args=(2,),name="immi")
t5 = Thread(target=f.reservation,args=(2,),name="raj")
t6 = Thread(target=f.reservation,args=(1,),name="ravi")

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()