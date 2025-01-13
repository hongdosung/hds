
import threading
import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == '__main__':
    multiprocessing.freeze_support()

    print('#### 멀티프로세싱 ####')

    ### 멀티프로세싱 ###
    # 멀티프로세싱은 여러 프로세스를 사용하여 동시에 여러 작업을 수행하는 방법입니다. 
    # 파이썬의 multiprocessing 모듈을 사용하여 멀티프로세싱을 구현할 수 있습니다. 
    # 프로세스는 각기 독립적인 메모리 공간을 가지므로 GIL의 영향을 받지 않으며, CPU 바운드 작업에서 성능 향상을 기대할 수 있습니다.

    # 프로세스 생성
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # 프로세스 시작
    p1.start()
    p2.start()

    # 프로세스가 종료될 때까지 대기
    p1.join()
    p2.join()

    print("Both processes have finished execution.")