from threading import Thread, current_thread, Semaphore
from time import sleep

class Flight:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.l = Semaphore(2)   # allow 2 threads at once
        
    def reserve(self, need_seat):
        with self.l:   # safer than acquire/release
            name = current_thread().name
            print(f"{name} entered → available seats: {self.available_seats}")
            
            if self.available_seats >= need_seat:
                print(f"Reservation confirmed for {name}")
                self.available_seats -= need_seat
                sleep(3)
                
            else:
                print(f"NOT enough seats for {name.upper()}")
            
            print(f"{name} leaving...")
            print()

f = Flight(3)
t1 = Thread(target=f.reserve, args=(1,), name="Martodkar")
t2 = Thread(target=f.reserve, args=(1,), name="Zunaisha")
t3 = Thread(target=f.reserve, args=(1,), name="Afreen")
t4 = Thread(target=f.reserve, args=(1,), name="Dilnaz")

t1.start()
t2.start()
t3.start()
t4.start()
