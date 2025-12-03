from threading import Thread,current_thread,Lock

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock() # add lock 
    
    def reserve(self,need_seat):
        self.l.acquire() # locking from here 
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

myt = Flight(4)
t1 = Thread(target=myt.reserve,args=(1,),name="Irfan")
t2 = Thread(target=myt.reserve,args=(1,),name="guddu")
t3 = Thread(target=myt.reserve,args=(1,),name="shakil")
t4 = Thread(target=myt.reserve,args=(1,),name="zunaisha")
t5 = Thread(target=myt.reserve,args=(1,),name="vicky")

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
