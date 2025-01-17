# 파이썬은 멀티스레딩과 멀티프로세싱을 통해 병렬 처리를 지원합니다.
# 이를 통해 CPU 사용률을 극대화하고, 대규모 데이터 처리 및 복잡한 연산을 더 빠르게 수행할 수 있습니다.
# [멀티스레딩]
# 멀티스레딩은 여러 스레드를 사용하여 동시에 여러 작업을 수행하는 방법입니다. 
# 파이썬의 threading 모듈을 사용하여 멀티스레딩을 구현할 수 있습니다. 
# 스레드는 동일한 메모리 공간을 공유하기 때문에 데이터 공유와 통신이 용이합니다. 
# 그러나 GIL(Global Interpreter Lock) 때문에 CPU 바운드 작업에서는 성능 향상이 제한적일 수 있습니다

# 프로그램 → 프로세스 → 스레드
# 프로그램이란, 파일이 저장 장치에 저장되어 있지만 메모리에는 올라가 있지 않은 정적인 상태를 말한다.
# 프로세스: 운영체제로부터 자원을 할당받은 작업의 단위. 실행되고 있는 컴퓨터 프로그램
# 스레드  : 프로세스가 할당받은 자원을 이용하는 실행 흐름의 단위. 스레드는 코드 내에 선언된 함수들이 되고 따라서 main 함수 또한 일종의 스레드

# 멀티태스킹이란, 하나의 운영체제 안에서 여러 프로세스가 실행되는 것을 의미한다.
# 멀티스레드는 하나의 프로세스가 여러 작업을 여러 스레드를 사용하여 동시에 처리하는 것을 의미한다.add()

# [멀티스레드의 단점]
# 스레드 하나가 프로세스 내 자원을 망쳐버린다면 모든 프로세스가 종료될 수 있다.
# 자원을 공유하기 때문에 필연적으로 동기화 문제가 발생할 수밖에 없다

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

# 스레드 생성
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# 스레드 시작
t1.start()
t2.start()

# 스레드가 종료될 때까지 대기
t1.join()
t2.join()

print("Both threads have finished execution.")
print(f"{'='*100}\n")

# sys.exit()


# 스레드 동기화
# 여러 스레드가 동시에 접근할 때 데이터의 일관성을 유지하려면 스레드 동기화가 필요합니다. 
# 파이썬의 threading 모듈은 동기화를 위해 Lock 객체를 제공합니다.

lock = threading.Lock()
counter = 0

def time_check(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")
    return wrapper

@time_check
def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = []
for _ in range(2):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
print(f"{'='*100}\n")

#sys.exit()


if __name__ == '__main__':
    multiprocessing.freeze_support() # 윈도우에서 필요한 코드 => RuntimeError 가 발생할 수 있습니다.

    print('#### 멀티프로세싱 ####')

    ### 멀티프로세싱 ###
    # 멀티프로세싱은 여러 프로세스를 사용하여 동시에 여러 작업을 수행하는 방법입니다. 
    # 파이썬의 multiprocessing 모듈을 사용하여 멀티프로세싱을 구현할 수 있습니다. 
    # 프로세스는 각기 독립적인 메모리 공간을 가지므로 GIL의 영향을 받지 않으며, CPU 바운드 작업에서 성능 향상을 기대할 수 있습니다.

    # 프로세스 생성
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=print_numbers)
        processes.append(process)
        process.start()

    # 프로세스가 종료될 때까지 대기
    for process in processes:
        process.join()
        #pass
    
    print("Both processes have finished execution")
    print(f"{'='*100}\n")