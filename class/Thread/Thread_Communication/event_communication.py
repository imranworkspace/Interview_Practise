from threading import Thread,Event
from time import sleep
'''Use Event → when signaling only
(e.g., telling threads to start/stop)
'''


def traffic_switch():
    sleep(5) # sleep for 5 seconds
    e.set()  # e is object of an event, set() return True status 
    print("Green Light ON")
    sleep(10) # wait for 3 seconds 
    print("Red Light ON")
    sleep(7)
    e.clear() # clear() use for Thread-1 execution is completed, now status=False, next thread will execute after that


def traffic():
    e.wait() # wait() function call when event is set= ex. e.set()
    while e.is_set():
        print("Signal is green --->>  you can go.....")
        sleep(.5)  # wait for 0.5 seconds 


    print("Thread Communication Event Is Completed")
e = Event()

t1 = Thread(target=traffic_switch)
t2 = Thread(target=traffic)

t1.start()
t2.start()