from threading import Thread,current_thread

class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
    
    def reserve(self,need_seat):
        print(f'available seat is {self.available_seat}')        
        if self.available_seat >= need_seat:
            name = current_thread().name 
            print(f'need of seat {need_seat}, seat allowcated to {name}')
            self.available_seat -= need_seat
        else:
            print('-----')
            print('sorry seats full..')

myt = Flight(1)
t1 = Thread(target=myt.reserve,args=(1,),name="Irfan")
t2 = Thread(target=myt.reserve,args=(1,),name="vicky")

t1.start()
t2.start()

#out put wrong  for currection see threadRace_synchronization.py program 
'''

available seat is 1
need of seat 1, seat allowcated to Irfan
available seat is 1
-----
sorry seats full..

'''