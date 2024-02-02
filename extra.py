
import pickle
f=open('myfile.txt','wb') 
d={1:'imran'}
ser=pickle.dump(d,f)
print('pickling done')
f.close()

with open('myfile.txt','rb') as f:
    des = pickle.load(f)
    print(des)