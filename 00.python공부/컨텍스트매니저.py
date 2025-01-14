# @ 컨텍스트 매니저
# 컨텍스트 매니저는 자원 관리를 위해 고안된 파이썬의 강력한 기능입니다. 
# 주로 파일, 네트워크 연결, 락(lock)과 같은 자원을 사용하고 나서 자동으로 정리(해제)하는데 사용됩니다. 
# 컨텍스트 매니저는 with 문과 함께 사용되며, 코드 블록의 진입과 종료 시 특정 작업을 수행할 수 있게 합니다. 
# 
# [기본 개념]
# 컨텍스트 매니저는 두 가지 주요 메서드인 __enter__와 __exit__를 구현해야 합니다. 
# __enter__ 메서드는 with 블록에 진입할 때 실행되며, __exit__ 메서드는 with 블록을 벗어날 때 실행됩니다.


# 사용자 정의 컨텍스트 매니저를 구현하려면 __enter__와 __exit__ 메서드를 포함하는 클래스를 정의하면 됩니다.
# 데이터베이스 연결을 관리하는 컨텍스트 매니저를 구현해 보겠습니다.


from contextlib import contextmanager
import time

class DatabaseConnection:
    def __enter__(self):
        print("Connecting to the database...")
        self.connection = self._connect_to_db()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing the database connection...")
        self.connection.close()

    def _connect_to_db(self):
        # 실제 데이터베이스 연결 로직을 여기에 작성합니다.
        class Connection:
            def close(self):
                print("Database connection closed.")
            print("kkkk")
        return Connection()

# 컨텍스트 매니저 사용
with DatabaseConnection() as conn:
    print("Using the database connection.")

# 위 코드에서 DatabaseConnection 클래스는 데이터베이스 연결을 관리하는 컨텍스트 매니저를 제공합니다. 
# __enter__ 메서드는 데이터베이스에 연결하고, __exit__ 메서드는 연결을 종료합니다.
print(f"{'='*100}\n")

# 예제: 파일 쓰기 컨텍스트 매니저
@contextmanager
def open_file(file_name, mode):
    file = open(file_name, mode, encoding='utf-8')
    try:
        yield file
    finally:
        file.close()

# 컨텍스트 매니저 사용
with open_file('hds\example_dir\hds_20241224.txt', 'w') as file:
    file.write('Hello, world!\n')

print(f"{'='*100}\n")


# 예제: 타이머 컨텍스트 매니저
@contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time:.4f} seconds")

# 컨텍스트 매니저 사용
with timer() as t:
    for _ in range(1000000):
        pass

print(f"{'='*100}\n")


@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")

# Usage
with my_context_manager() as my:
    print("Inside the context")

print(f"{'='*100}\n")


# 컨텍스트 매니저는 자원의 획득과 해제를 자동으로 처리하여 코드의 가독성과 안전성을 높여주는 강력한 도구입니다.
# with 문을 사용하여 컨텍스트 매니저를 적용하면, 코드 블록 진입 시와 종료 시 자동으로 필요한 작업을 수행
# 사용자 정의 컨텍스트 매니저를 작성하거나 contextlib 모듈을 사용하여 간단한 컨텍스트 매니저를 쉽게 구현할 수 있습니다
# 이러한 기능을 잘 활용하면 자원 관리가 필요한 다양한 상황에서 코드를 간결하고 안전하게 작성할 수 있습니다.
