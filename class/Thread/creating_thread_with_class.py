from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print('child thread')

t = MyThread()
t.start()
t.join()

for i in range(5):
    print('main thread')