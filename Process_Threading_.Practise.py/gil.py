import threading

# A shared counter variable
counter = 0

def increment_counter():
    global counter
    for _ in range(1000000):
        counter += 1

def main():
    # Create two threads
    thread1 = threading.Thread(target=increment_counter)
    thread2 = threading.Thread(target=increment_counter)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    # Print the final value of the counter
    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
