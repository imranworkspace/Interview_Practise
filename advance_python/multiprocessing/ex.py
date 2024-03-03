import multiprocessing
import requests
import time
import concurrent.futures
def downloadImage(url,name):
    print(f'download started {name}')
    reps = requests.get(url)
    open(f"images/{name}.jpg",'wb').write(reps.content)
    print(f'finished downloading {name}')

if __name__=="__main__":
    time1=time.perf_counter()
    print('process started')
    url="https://picsum.photos/200/300"
    # process_ids = []
    # for i in range(100):
    #     p1=multiprocessing.Process(target=downloadImage,args=[url,i])
    #     p1.start()
    #     process_ids.append(p1)
    # time2=time.perf_counter()
    # es=time2-time1
    # print('total time {}'.format(es))

    # # do joins
    # for j in process_ids:
    #     j.join()
# check your system performance
        
    # instead use Process Pool Executor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        url_lst=[url for i in range(160)] # url list 1st parameter
        name_lst=[limit for limit in range(160)]  # name list 1st parameter
        results = executor.map(downloadImage,url_lst,name_lst)
        for result in results:
            print(result)
    time2=time.perf_counter()
    print(time2-time1)
