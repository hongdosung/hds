# @ 컨텍스트 매니저
# 컨텍스트 매니저는 자원 관리를 위해 고안된 파이썬의 강력한 기능입니다. 
# 주로 파일, 네트워크 연결, 락(lock)과 같은 자원을 사용하고 나서 자동으로 정리(해제)하는데 사용됩니다. 
# 컨텍스트 매니저는 with 문과 함께 사용되며, 코드 블록의 진입과 종료 시 특정 작업을 수행할 수 있게 합니다. 
# 
# [기본 개념]
# 컨텍스트 매니저는 두 가지 주요 메서드인 __enter__와 __exit__를 구현해야 합니다. 
# __enter__ 메서드는 with 블록에 진입할 때 실행되며, __exit__ 메서드는 with 블록을 벗어날 때 실행됩니다.

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")

# Usage
with my_context_manager():
    print("Inside the context")

print(f"{'='*100}\n")
    

@contextmanager
def open_file(file_name, mode, encoding='utf-8'):
    file = open(file_name, mode, encoding='utf-8')
    try:
        yield file
    finally:
        file.close()

# 컨텍스트 매니저 사용
with open_file('hds\example_dir\hds_20241224.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, world!')

print(f"{'='*100}\n")
    
# 사용자 정의 컨텍스트 매니저를 구현하려면 __enter__와 __exit__ 메서드를 포함하는 클래스를 정의하면 됩니다.
# 데이터베이스 연결을 관리하는 컨텍스트 매니저를 구현해 보겠습니다.

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
        return Connection()

# 컨텍스트 매니저 사용
with DatabaseConnection() as conn:
    print("Using the database connection.")

# 위 코드에서 DatabaseConnection 클래스는 데이터베이스 연결을 관리하는 컨텍스트 매니저를 제공합니다. 
# __enter__ 메서드는 데이터베이스에 연결하고, __exit__ 메서드는 연결을 종료합니다.


print(f"{'='*100}\n")