from threading import Thread,current_thread,Semaphore,BoundedSemaphore

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        # self.l = Semaphore(2) # semaphore - synchronize lock allow 2 threads lock at the same time  
        self.l = BoundedSemaphore(2) # Bounded semaphore - synchronize lock allow 2 threads lock at the same time  
    
    def reserve(self,need_seat):
        self.l.acquire() # locking from here 
        # self.l._value() # show semaphore value 
        print(f'available seat is {self.available_seat}')        
        if self.available_seat >= need_seat:
            name = current_thread().name 
            print(f'need of seat {need_seat}, seat allowcated to {name}')
            self.available_seat -= need_seat
            print()
        else:
            print('-----')
            print('sorry seats full..')
        self.l.release() # realising lock from here 

myt = Flight(2)
t1 = Thread(target=myt.reserve,args=(1,),name="Irfan")
t2 = Thread(target=myt.reserve,args=(1,),name="guddu")
t3 = Thread(target=myt.reserve,args=(1,),name="shakil")


t1.start()
t2.start()
t3.start()
