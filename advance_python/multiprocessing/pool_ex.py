from multiprocessing import Pool
import time
def handle(arr_val):
    print(f'we got processer name {arr_val[0]} and value {arr_val[1]}')
    time.sleep(arr_val[1])
    print(f'execution completed {arr_val[0]}')

if __name__=="__main__":
    start_time = time.time()
    arr_val =(['V',1],['X',22],['y',15],['R',5],['S',4])
    p = Pool(3)
    p.map(handle,arr_val)
    end_time = time.time()
    end = end_time - start_time
    print('total time ',(end))