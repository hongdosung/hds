# 프로세스 간 통신
# 프로세스 간 통신을 위해 multiprocessing.Queue를 사용할 수 있습니다.
# Pool 클래스를 사용하여 여러 프로세스를 생성하고 관리할 수 있습니다.
# 파이프를 사용한 프로세스 간 통신
# 프로세스 간 통신을 위해 multiprocessing.Pipe를 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.Queue를 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.Value와 multiprocessing.Array를 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.Manager를 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.shared_memory를 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.connection을 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.sharedctypes을 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.sharedctypes을 사용할 수 있습니다.
# 프로세스 간 통신을 위해 multiprocessing.shared_memory을 사용할 수 있습니다.

import multiprocessing

def worker(queue):
    for i in range(5):
        queue.put(i)

def square(x):
    return x * x

def worker2(conn):
    conn.send("Hello from the worker process!")
    conn.close()

if __name__ == "__main__":
    # 프로세스 간 통신
    # multiprocessing.Queue를 사용하여 자식 프로세스가 생성한 데이터를 부모 프로세스에서 읽습니다.
    queue = multiprocessing.Queue() # 프로세스 간 통신을 위해 multiprocessing.Queue를 사용할 수 있습니다.
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    p.join()

    while not queue.empty():
        print(queue.get())
    
    # 풀을 사용한 작업 분배
    # 위 코드에서는 multiprocessing.Pool을 사용하여 square 함수를 병렬로 실행하고, 결과를 수집합니다.
    with multiprocessing.Pool(4) as pool: # Pool 클래스를 사용하여 여러 프로세스를 생성하고 관리할 수 있습니다.
        results = pool.map(square, range(10))
    print(results)
    
    
    # 파이프를 사용한 프로세스 간 통신
    parent_conn, child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(target=worker2, args=(child_conn,))
    process.start()
    
    print(parent_conn.recv())  # Receive the message from the worker process
    process.join()
