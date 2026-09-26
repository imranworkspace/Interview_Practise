import time
import threading
from concurrent.futures import ThreadPoolExecutor


def fun(n):
    print(f"Wait for {n} seconds")
    time.sleep(n)
    return n


# # -------------------------
# # Sequential version
# # -------------------------
s1 = time.perf_counter()

fun(10)
fun(4)
fun(2)
fun(1)

e1 = time.perf_counter()

print(f"Time taken for sequential process: {e1 - s1:.2f} seconds")
print()


# -------------------------
# Threading version
# -------------------------
s2 = time.perf_counter()

t1 = threading.Thread(target=fun, args=(10,))
t2 = threading.Thread(target=fun, args=(4,))
t3 = threading.Thread(target=fun, args=(2,))
t4 = threading.Thread(target=fun, args=(1,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

e2 = time.perf_counter()

print(f"Time taken for threading process: {e2 - s2:.2f} seconds")
print()


# -------------------------
# ThreadPoolExecutor version
# -------------------------
if __name__ == "__main__":

    s3 = time.perf_counter()

    timer_lst = (10, 4, 2, 1)

    with ThreadPoolExecutor(max_workers=4) as executor:

        futures = [
            executor.submit(fun, i)
            for i in timer_lst
        ]

        for future in futures:
            try:
                result = future.result()
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

    e3 = time.perf_counter()

    print(f"Time taken for ThreadPoolExecutor process: {e3 - s3:.2f} seconds")