
import threading
import multiprocessing
import time

# Function to be executed in a thread
def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")

# Function to be executed in a process
def process_function(name):
    print(f"Process {name}: starting")
    time.sleep(2)
    print(f"Process {name}: finishing")

if __name__ == "__main__":
    multiprocessing.freeze_support() # 윈도우에서 필요한 코드 => RuntimeError 가 발생할 수 있습니다.
    
    # Creating and starting threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    # Creating and starting processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=process_function, args=(i,))
        processes.append(process)
        process.start()

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()

    # Waiting for all processes to complete
    for process in processes:
        process.join()

    print("All threads and processes have finished.")
