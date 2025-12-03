from threading import Thread,current_thread,RLock
from time import sleep

class Flight:
    def __init__(self,available_seats):
        self.available_seats = available_seats
        self.l = RLock()

        
    def reserve(self,need_seat):
        self.l.acquire()
        name = current_thread().name
        print('available seats are : -> ',self.available_seats)
        if self.available_seats >= need_seat:
            
            print(f'reservation confirmed of {name}')
            self.available_seats -= need_seat
            sleep(5)            
        else:
            print()
            print(f'Seat are not available {name.upper()}...you can book another flight')
        self.l.release()
f = Flight(2)
t1=Thread(target=f.reserve,args=(1,),name="Martodkar")
t2=Thread(target=f.reserve,args=(1,),name="Zunaisha")
t3=Thread(target=f.reserve,args=(1,),name="Afreen")

t1.start()      
t2.start()      
t3.start()      