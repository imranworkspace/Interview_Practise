from threading import Thread

class MyThread(Thread):
    def __init__(self,val):
        Thread.__init__(self) # must be add for constructor 
        self.val = val

    def run(self):
        for i in range(5):
            print('child thread',self.val)

t = MyThread(10)
t.start()
t.join()

for i in range(5):
    print('main thread')