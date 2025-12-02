from threading import Thread, Condition
from time import sleep
from queue import Queue
# Condition is thread safe (maintaining automatic lock)
# method = put(),get(),empty() and full()

'''
Use Queue → when exchanging data safely
(best and simplest for producer/consumer)
'''
class Producer:
    def __init__(self):
        self.q = Queue()
    
    def produce(self):
        for i in range(1,6):
            print('Item Produced ',i)
            self.q.put(i) # put use
            sleep(1)

class Consumer:
    def __init__(self,prod):
        self.prod = prod
    
    def consume(self):
        for _ in range(1,6):
            item = self.prod.q.get() # get produce variable
            print('Item Consumed - ',item)
            print()
prod = Producer()
cons = Consumer(prod)

t1 = Thread(target=prod.produce)
t2 = Thread(target=cons.consume)

t1.start()
t2.start()