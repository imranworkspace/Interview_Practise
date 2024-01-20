import multiprocessing

def increment_counter(counter, iterations):
    for _ in range(iterations):
        counter.value += 1

def main():
    # Use multiprocessing.Value to create a shared counter variable
    counter = multiprocessing.Value('i', 0)

    # Create two processes
    process1 = multiprocessing.Process(target=increment_counter, args=(counter, 1000000))
    process2 = multiprocessing.Process(target=increment_counter, args=(counter, 1000000))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    # Print the final value of the counter
    print("Final counter value:", counter.value)

if __name__ == "__main__":
    main()
