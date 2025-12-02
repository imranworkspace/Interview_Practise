from threading import Thread
import time
class MyThread:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()
    
    def q1(self):
        time.sleep(3)
        print('q1 is solved')
    def q2(self):
        time.sleep(3)
        print('q2 is solved')
    def q3(self):
        time.sleep(3)
        print('q3 is solved')

myt = MyThread()
t = Thread(target=myt.solve_question)
t.start()