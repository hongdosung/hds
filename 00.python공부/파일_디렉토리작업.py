# 디렉토리 내에서 특정 패턴을 가진 파일을 검색하려면 glob 모듈을 
# 경로를 결합하려면 os.path.join() 함수
# 절대 경로를 얻으려면 os.path.abspath() 함수를 사용
# 경로를 디렉토리와 파일명으로 분리하려면 os.path.split() 함수를 사용
# os.getcwd() 를 통해 현재 작업하고 있는 폴더를 알 수 있다.
# os.chdir(경로) 를 통해 현재 작업 폴더를 변경할 수 있다.
# os.listdir(경로) 를 통해 경로의 파일과 폴더 목록을 확인할 수 있다.
# os.path.exists(경로) 를 통해 해당 경로가 존재하는지 확인할 수 있다.
# os.path.isfile(경로) 를 통해 해당 경로가 파일인지 확인할 수 있다.
# os.path.isdir(경로) 를 통해 해당 경로가 폴더인지 확인할 수 있다.
# os.mkdir(경로) 를 통해 해당 경로에 폴더를 생성할 수 있다.
# os.makedirs(경로) 를 통해 해당 경로의 상위 폴더까지 생성할 수 있다.
# os.remove(경로) 를 통해 해당 경로의 파일을 삭제할 수 있다.
# os.rmdir(경로) 를 통해 해당 경로의 폴더를 삭제할 수 있다.
# shutil.rmtree(경로) 를 통해 해당 경로의 폴더와 파일을 모두 삭제할 수 있다.
# os.rename(기존 경로, 새 경로) 를 통해 파일 또는 폴더의 이름을 변경할 수 있다.
# os.walk(경로) 를 통해 해당 경로의 하위 폴더와 파일을 탐색할 수 있다.
# os.path.join(경로1, 경로2) 를 통해 경로를 결합할 수 있다.
# os.path.abspath(경로) 를 통해 절대 경로를 얻을 수 있다.
# os.path.split(경로) 를 통해 경로를 디렉토리와 파일명으로 분리할 수 있다.
# glob.glob(패턴) 를 통해 디렉토리 내에서 특정 패턴을 가진 파일을 검색할 수 있다.
# shutil.move(기존 경로, 새 경로) 를 통해 파일을 이동할 수 있다.
# shutil.copy(기존 경로, 새 경로) 를 통해 파일을 복사할 수 있다.
# shutil.copytree(기존 경로, 새 경로) 를 통해 폴더를 복사할 수 있다.
# shutil.rmtree(경로) 를 통해 폴더와 파일을 모두 삭제할 수 있다.
# shutil.make_archive(압축 파일명, 압축 포맷, 압축할 폴더) 를 통해 폴더를 압축할 수 있다.
# shutil.unpack_archive(압축 파일명, 해제할 폴더) 를 통해 압축 파일을 해제할 수 있다.
# os.chmod(파일명, 권한) 를 통해 파일의 권한을 설정할 수 있다.
# os.path.getsize(파일명) 를 통해 파일의 크기를 확인할 수 있다.
# os.path.getmtime(파일명) 를 통해 파일의 수정 시간을 확인할 수 있다.
# os.path.getctime(파일명) 를 통해 파일의 생성 시간을 확인할 수 있다.
# os.path.getatime(파일명) 를 통해 파일의 최근 접근 시간을 확인할 수 있다.
# os.path.splitext(파일명) 를 통해 파일의 확장자를 분리할 수 있다.
# os.path.dirname(경로) 를 통해 경로의 디렉토리 부분을 확인할 수 있다.
# os.path.basename(경로) 를 통해 경로의 파일명 부분을 확인할 수 있다.
# os.path.relpath(경로, 기준 경로) 를 통해 경로를 기준 경로를 기준으로 상대 경로로 변환할 수 있다.
#   os.path.relpath('C:\\Windows\\Fonts', 'C:\\Windows\\System32') -> '..\\Fonts'
# os.path.commonpath(경로 리스트) 를 통해 경로 리스트의 공통 경로를 확인할 수 있다.
# os.path.commonprefix(경로 리스트) 를 통해 경로 리스트의 공통 접두어를 확인할 수 있다.
# os.path.normpath(경로) 를 통해 경로의 정규화된 경로를 확인할 수 있다.
# os.path.realpath(경로) 를 통해 경로의 실제 경로를 확인할 수 있다.
# os.path.samefile(경로1, 경로2) 를 통해 두 경로가 같은 파일을 가리키는지 확인할 수 있다.
# os.path.isabs(경로) 를 통해 경로가 절대 경로인지 확인할 수 있다.
# os.path.basename('C:\\Windows\\System32\\notepad.exe') -> 'notepad.exe'
# os.path.exists(경로) 를 통해 경로가 존재하는지 확인할 수 있다.

import os
import glob
import shutil

# Create a new directory
def create_directory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{path}' created successfully")
        else:
            print(f"Directory '{path}' already exists")
    except FileExistsError:
        print(f"Directory '{path}' already exists")

# Create a new file
def create_file(path, file_nm, content=""):
    if os.path.exists(path):
        with open(f'{path}/{file_nm}', 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File '{file_nm}' created successfully")
    else:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully")
        with open(f'{path}/{file_nm}', 'w', encoding='utf-8') as file:
            file.write(content)

# List files and directories in a given path
def list_directory(path):
    try:
        items = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{path}' not found")

# Rename a file or directory
def rename_item(path, old_fn, new_fn):
    try:
        os.rename(os.path.join(path, old_fn), os.path.join(path, new_fn))
        print(f"'{old_fn}' renamed to '{new_fn}' successfully")
    except FileNotFoundError:
        print(f'{old_fn} not found')
    except FileExistsError:
        print(f"'{new_fn}' already exists")
    except Exception as e:
        print(f"Error renaming '{old_fn}' to '{new_fn}': {e}")

def move_file(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}.")
    else:
        print(f"Source file {src} does not exist.")


def search_file(directory, filename):
    try:
        file_path = os.path.join(directory, filename)
        print(f'search_file file_path: {file_path}')
        for root, dirs, files in os.walk(directory):
            print(f'root: {root}')
            print(f'dirs: {dirs}')
            if filename in files:
                print(f"File '{filename}' found in '{root}'")
                return os.path.join(root, filename)
        print(f"File '{filename}' not found in '{directory}'")
        return None
    except Exception as e:
        print(f"Error searching for '{filename}' in '{directory}': {e}")
        return None

# glob 모듈을 사용하여 디렉토리 내에서 특정 패턴을 가진 파일을 검색할 수 있습니다.
def search_glob_file(directory, filename):
    try:
        file_path = os.path.join(directory, filename)
        print(f'search_glob_file file_path: {file_path}')
        files = glob.glob(file_path) # 디렉토리 파일 목록 추출(단 경로까지 추출 ex: /경로/파일명)
        print(f'THE files in {directory}')
        for file in files:
            print(file)
        return None
    except Exception as e:
        print(f"Error glob searching for '{filename}' in '{directory}': {e}")
        return None

# Delete a file
def delete_file(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"File '{path}' deleted successfully")
        else:
            print(f"File '{path}' not found")
    except FileNotFoundError:
        print(f"File '{path}' not found")

# Delete a directory
def delete_directory(path):
    try:
        os.rmdir(path)
        print(f"Directory '{path}' deleted successfully")
    except FileNotFoundError:
        print(f"Directory '{path}' not found")
    except OSError:
        print(f"Directory '{path}' is not empty")

# Manipulate file pointer
def manipulate_file_pointer(file_path, position, content):
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            print(f'1 {file_path} => {file.read()}')
            file.seek(position) # 파일 포인터를 position 위치로 이동
            #print(f'2 ===> {file.read()}')
            print(f'file.tell() ===> {file.tell()}') # 현재 파일 포인터 위치 반환
            file.write(content)            
            file.seek(0)    
            print(f'3 ===> {file.read()}')
            print(f"Written '{content}' at position {position} in '{file_path}'")
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except Exception as e:
        print(f"Error manipulating file pointer in '{file_path}': {e}")


# Example usage
if __name__ == "__main__":
    dir_path = 'hds/example_dir'
    file_nm = 'example_file.txt'
    #create_directory(dir_path)
    create_file(dir_path, file_nm, 'Hello, world!!!!!!!')
    print('='*80+'\n')
    list_directory(dir_path)
    print('='*80+'\n')
    rename_item(dir_path, file_nm, 'new_file.txt')
    print('='*80+'\n')
    s_file = search_file(dir_path, file_nm)
    print(f'search_file: {s_file}')
    print('='*80+'\n')
    search_glob_file(dir_path, file_nm)
    print('='*80+'\n')
    # delete_file(f'{dir_path}/{file_nm}')
    # delete_directory(f'{dir_path}')
    
    # 절대 경로를 얻으려면 os.path.abspath() 함수를 사용
    absolute_path = os.path.abspath(os.path.join(dir_path, file_nm))
    print(f"Absolute path: {absolute_path}")
    
    # 경로를 디렉토리와 파일명으로 분리하려면 os.path.split() 함수를 사용    
    file_path = '/path/to/example.txt'
    directory, filename = os.path.split(file_path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    print('='*80+'\n')
    
    content = ' API_TEST HDS'
    manipulate_file_pointer(os.path.join(dir_path, file_nm), 20, content)


    # 파일을 읽기 및 쓰기 모드로 열기
    with open(f'{dir_path}/example17.txt', 'r+') as file:
        content = file.read()
        file.write('Additional content')

    # os.chmod('example.txt', 0o644)  # 읽기/쓰기 권한 설정