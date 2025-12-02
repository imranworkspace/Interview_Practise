from threading import Thread

class MyThread:
    def disp(self,a,b):
        print(a+b)

myt = MyThread()
t = Thread(target=myt.disp,args=(10,20))
t.start()
