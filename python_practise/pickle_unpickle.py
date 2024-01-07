import pickle
d={1:'imran',2:'irfan'}
f=open('demo.txt','wb')
seri = pickle.dump(d,f)
print('pickling complted')
f.close()

f1=open('demo.txt','rb')
deseri = pickle.load(f1)
print(deseri)
print('unpickling complted')
f1.close()

