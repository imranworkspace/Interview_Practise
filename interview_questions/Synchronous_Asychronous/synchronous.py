import time 
def task(n):
    print(f"started task {n}")
    time.sleep(2)
    print(f'finished task {n}')
    print('-----')

def main():
    task(1)
    task(2)
    task(3)

main()