# 파일 읽기
# 파일에서 데이터를 읽으려면 read(), readline(), readlines() 메소드를 사용합니다.
# [모드	설명]
#  r -> 읽기 전용 모드로 파일을 엽니다. 파일이 존재하지 않으면 오류가 발생합니다.
#  w -> 쓰기 전용 모드로 파일을 엽니다. 파일이 존재하면 내용을 덮어쓰고, 파일이 존재하지 않으면 새로 만듭니다.
#  a -> 추가 모드로 파일을 엽니다. 파일이 존재하지 않으면 새로 만듭니다. 파일 끝에 내용을 추가합니다.
#  b -> 이진 모드로 파일을 엽니다. 다른 모드와 함께 사용됩니다. 예: rb 또는 wb
#  x -> 배타적 생성 모드로 파일을 엽니다. 파일이 존재하지 않으면 새로 만들고, 파일이 이미 존재하면 오류가 발생합니다.
#  + -> 읽기와 쓰기 모드를 모두 허용합니다. 다른 모드와 함께 사용됩니다. 예: r+, w+, a+
# os.chmod('example.txt', 0o644)  # 읽기/쓰기 권한 설정

# 파일 읽기 및 쓰기: 로그 파일에 데이터를 기록하고, 필요할 때 파일을 읽어오는 기능을 구현합니다.
# 파일 포인터 조작: 파일 포인터를 이동시켜 특정 위치의 데이터를 읽어옵니다.
# 대용량 파일 처리: 대용량 로그 파일을 한 줄씩 처리하여 특정 패턴을 검색합니다.
# 임시 파일 사용: 임시 파일을 사용하여 중간 데이터를 처리합니다.
# 압축 파일 처리: 로그 파일을 압축하여 백업하고, 백업된 파일을 해제합니다.
# 파일 권한 설정: 로그 파일의 권한을 설정하여 보안을 강화합니다.


import os
import csv
import json
import tempfile # 임시 파일 및 디렉토리 생성
import zipfile # ZIP 파일 압축 및 해제


# 학생 성적 데이터
students = [
    {'name': 'Alice', 'math': 90, 'science': 85, 'english': 88},
    {'name': 'Bob', 'math': 78, 'science': 81, 'english': 92},
    {'name': 'Charlie', 'math': 95, 'science': 89, 'english': 85}
]

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        return f"Attribute 1 is {self.attribute1} 홍도성1"

    def method2(self):
        return f"Attribute 2 is {self.attribute2} 홍도성2"
    
    def method3(self):
        return f"Attribute 3 is {self.attribute2} 홍도성3"

def process(line):
    # 한 줄씩 처리하는 로직을 여기에 작성합니다.
    print(f"Processing line: {line.strip()}")

# Example usage
if __name__ == "__main__":
    obj = MyClass("value1", "value2")
    print(obj.method1())
    print(obj.method2())
    print(obj.method3())
    
    dir_path = 'hds/example_dir'
    
    # Writing to a file
    with open(f"{os.path.join(dir_path, 'output.txt')}", "w", encoding='utf-8') as file:
        file.write(obj.method1() + "\n")
        file.write(obj.method2() + "\n")
        file.write(obj.method3() + "\n")

    # file 전체 읽기
    with open(f"{os.path.join(dir_path, 'output.txt')}", "r", encoding='utf-8') as file:
        content = file.read()
        print("\n=== File content ===")
        print(content)    
    
    # file 한줄씩 읽기
    with open(f"{os.path.join(dir_path, 'output.txt')}", "r", encoding='utf-8') as file:
        line = file.readline().strip()
        while line:
            #print(line, end='') # 줄바꿈 제거
            print(f'line: {line}')
            line = file.readline().strip()
            
    # 파일 전체를 줄 단위로 읽기  
    with open(f"{os.path.join(dir_path, 'output.txt')}", 'r', encoding='utf-8') as file:
        lines = file.readlines() 
        for line in lines:
            print(line, end='') # 줄바꿈 제거
            #print(f'line2: {line}')
    print('='*80+'\n')

    # CSV 파일 처리
    csv_file = 'data.csv'

    # CSV 파일 쓰기
    with open(f'{os.path.join(dir_path, csv_file)}', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Column1', 'Column2', 'Column3'])
        writer.writerow(['Value1', 'Value2', 'Value3'])
        writer.writerow(['Value4', 'Value5', 'Value6'])
        writer.writerow(obj.method1())

    # CSV 파일 읽기
    with open(f'{os.path.join(dir_path, csv_file)}', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            #print(', '.join(row))
    print('='*80+'\n')
    
    # CSV 파일에 학생 성적 데이터 쓰기
    with open(f"{os.path.join(dir_path, 'students.csv')}", 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'math', 'science', 'english'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

    # CSV 파일에서 학생 성적 데이터 읽기
    with open(f"{os.path.join(dir_path, 'students.csv')}", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        #header = next(reader)
        for row in reader:
            print(row)
                    
    print('='*80+'\nDictReader')
        
    # CSV 파일에서 학생 성적 데이터 읽기
    with open(f"{os.path.join(dir_path, 'students.csv')}", 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            #print(row)
            print(row['name'], row['math'], row['science'], row['english'])
    print('='*80+'\n')

    # JSON 파일 처리
    json_file = 'data.json'
    data = {
        'name': '홍길동',
        'age': 30,
        'city': '서울'
    }

    print('==== JSON ====')
    # JSON 파일 쓰기
    with open(f'{os.path.join(dir_path, json_file)}', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        #json.dumps(data, ensure_ascii=False)

    # JSON 파일 읽기
    with open(f'{os.path.join(dir_path, json_file)}', 'r', encoding='utf-8') as file:
        data = json.load(file)
        #data = json.loads(file)
        print(data)
    print('='*80+'\n')
    
    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)
    json_data2 = json.loads(json_data)
    print(json_data2)
    json_data3 = json.loads(json.dumps(data))
    print(json_data3)
    print()
    
    print('==== 대용량 파일처리 ====')
    # 대용량 파일처리
    with open(f'{dir_path}\output.txt', 'r', encoding='utf-8') as file:
        for line in file:
            #process(line) # 한 줄씩 읽어 처리
            print(f"Pro line: {line.strip()}")
    print('='*80+'\n')

    # 대용량 파일처리
    with open(f'{dir_path}\output.txt', 'r', encoding='utf-8') as file:
        for line in file:
            process(line) # 한 줄씩 읽어 처리
    print('='*80+'\n')
    
    # 파일을 읽기 및 쓰기 모드로 열기
    with open(f'{dir_path}\example.txt', 'r+') as file:
        content = file.read()
        file.write('Additional content\n')
    
    #### 임시 파일 및 디렉토리 작업 ####
    # 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'This is a temporary file.')
        print(f"Temporary file created at {temp_file.name}")

    # 임시 디렉토리 생성
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Temporary directory created at {temp_dir}")
        
    #### ZIP 파일 압축 및 해제 ####
    # zipfile과 tarfile 모듈을 사용하여 압축 파일을 생성하고 해제하는 방법
    # ZIP 파일 생성
    with zipfile.ZipFile(f'{dir_path}/zip/zip_example.zip', 'w') as zipf:
        zipf.write(f'{dir_path}\data.csv')
        zipf.write(f'{dir_path}\data.json')
        zipf.write(f'{dir_path}\students.csv')
        zipf.write(f'{dir_path}\output.txt')
        zipf.write(f'{dir_path}\example_file.txt')
        zipf.write(f'{dir_path}\hds.txt')
        zipf.write(f'{dir_path}\do3.txt')
        zipf.write(f'{dir_path}\knew_file2.txt')

    # ZIP 파일 읽기
    with zipfile.ZipFile(f'{dir_path}/zip/zip_example.zip', 'r') as zipf:
        zipf.extractall('zip_extracted_files')
