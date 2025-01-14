import threading
import multiprocessing
import time
import sys

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)


if __name__ == '__main__':
    multiprocessing.freeze_support() # 윈도우에서 필요한 코드 => RuntimeError 가 발생할 수 있습니다.

    print('#### 멀티프로세싱 ####')

    ### 멀티프로세싱 ###
    # 멀티프로세싱은 여러 프로세스를 사용하여 동시에 여러 작업을 수행하는 방법입니다. 
    # 파이썬의 multiprocessing 모듈을 사용하여 멀티프로세싱을 구현할 수 있습니다. 
    # 프로세스는 각기 독립적인 메모리 공간을 가지므로 GIL의 영향을 받지 않으며, CPU 바운드 작업에서 성능 향상을 기대할 수 있습니다.

    # 멀티 프로세스 생성
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=print_numbers)
        processes.append(p)
        p.start()

    # 멀티 프로세스가 종료될 때까지 대기
    for process in processes:
        process.join()
    
    print("Both processes have finished execution")
    print(f"{'='*100}\n")
    
    # 멀티 스레트 생성
    threads = []
    for i in range(3):
        t = threading.Thread(target=print_letters)
        threads.append(t)
        t.start()
    
    # 멀티 스레드가 종료될 때까지 대기
    for thread in threads:
        thread.join()   
    
    print("Both threads have finished execution")
    print(f"{'='*100}\n")