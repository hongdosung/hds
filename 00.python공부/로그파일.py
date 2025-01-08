import os
from datetime import datetime
import tempfile
import zipfile

#### 로그 파일에 메시지를 작성하는 함수를 작성s
def write_log(message):
    log_dir = 'hds/logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')
    with open(log_file, 'a', encoding='utf-8') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - {message}\n")
    print(f"Log written: {message}")

# 예제 실행
write_log("Application started")
write_log("An error occurred")

def read_log(offset, length):
    log_file = 'hds/logs/app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as file:
            file.seek(offset)
            data = file.read(length)
            print("================================================================")
            print(f"Read data: {data}")            
            print("================================================================")
    else:
        print("Log file does not exist")

# 예제 실행
read_log(0, 1000)

#### 대용량 로그 파일을 한 줄씩 처리하여 특정 패턴을 검색하는 함수를 작성
def search_in_log(pattern):
    log_file = 'hds/logs/app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if pattern in line:
                    print(f"Found pattern: {line.strip()}")
    else:
        print("Log file does not exist")

# 예제 실행
search_in_log("error")


#### 임시 파일 사용
# 임시 파일을 사용하여 중간 데이터를 처리하고, 파일을 자동으로 삭제하는 예제를 작성합니다.
# 임시 디렉토리 생성
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at {temp_dir}")

def process_with_temp_file(data):
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        print(f"temp_file.name: {temp_file.name}")
        temp_file.write(data.encode())
        temp_file.seek(0)
        processed_data = temp_file.read().decode()
        print(f"Processed data: {processed_data}")

# 예제 실행
process_with_temp_file("Temporary data processing")


#### 압축 파일 처리
# 로그 파일을 압축하여 백업하고, 백업된 파일을 해제하는 함수를 작성합니다.
def backup_logs():
    log_dir = 'hds/logs'
    backup_dir = 'hds/backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, 'logs_backup.zip')
    with zipfile.ZipFile(backup_file, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(log_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, log_dir))
    print(f"Logs backed up to {backup_file}")

def extract_backup():
    backup_file = 'hds/backup/logs_backup.zip'
    extract_dir = 'hds/extracted_logs'
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    with zipfile.ZipFile(backup_file, 'r') as zipf:
        zipf.extractall(extract_dir)
    print(f"Logs extracted to {extract_dir}")

# 예제 실행
backup_logs()
extract_backup()

#### 파일 권한 설정
# 로그 파일의 권한을 설정하여 보안을 강화하는 예제를 작성합니다.

def set_log_file_permissions():
    log_file = 'hds/logs/app.log'
    if os.path.exists(log_file):
        os.chmod(log_file, 0o600)  # 소유자 읽기/쓰기 권한 설정
        print(f"Permissions set for {log_file}")

# 예제 실행
set_log_file_permissions()