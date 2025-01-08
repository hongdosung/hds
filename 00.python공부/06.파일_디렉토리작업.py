# 디렉토리 내에서 특정 패턴을 가진 파일을 검색하려면 glob 모듈을 
# 경로를 결합하려면 os.path.join() 함수
# 절대 경로를 얻으려면 os.path.abspath() 함수를 사용
# 경로를 디렉토리와 파일명으로 분리하려면 os.path.split() 함수를 사용


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
        print(f"Directory '{os.path.dirname(path)}' not found")
        
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
        os.rename(f'{os.path.join(path, old_fn)}', f'{os.path.join(path, new_fn)}')
        print(f"'{old_fn}' renamed to '{new_fn}' successfully")
    except FileNotFoundError:
        print(f"'{old_fn}' not found")
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

def search_glob_file(directory, filename):
    try:
        file_path = os.path.join(directory, filename)
        print(f'search_glob_file file_path: {file_path}')
        files = glob.glob(os.path.join(directory, filename))
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
        os.remove(path)
        print(f"File '{path}' deleted successfully")
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
            print(f'1 ===> {file.read()}')
            file.seek(position)
            print(f'2 ===> {file.read()}')
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
    create_directory(f'{dir_path}')
    create_file(f'{dir_path}', f'{file_nm}', 'Hello, world!')
    list_directory(f'{dir_path}')
    rename_item(f'{dir_path}', f'{file_nm}', 'new_file.txt')
    search_file(dir_path, file_nm)
    search_glob_file(dir_path, file_nm)
    # delete_file(f'{dir_path}/{file_nm}')
    # delete_directory(f'{dir_path}')
    
    relative_path = 'example.txt'
    absolute_path = os.path.abspath(relative_path)
    print(f"Absolute path: {absolute_path}")
    
    file_path = '/path/to/example.txt'
    directory, filename = os.path.split(file_path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
    
    content = 'API_TEST HDS'
    manipulate_file_pointer(f'{os.path.join(dir_path, file_nm)}', 30, f'{content}')
    