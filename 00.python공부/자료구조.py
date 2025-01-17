# 학생 정보 저장 (리스트)
students = [
    {"name": "Alice", "scores": (90, 85, 88)},
    {"name": "Bob", "scores": (78, 81, 92)},
    {"name": "Charlie", "scores": (95, 89, 85)}
]

# 특정 학생의 정보 조회 (딕셔너리)
def get_student_info(name):
    for student in students:
        if student["name"] == name:
            return student
    return None

# 과목별 최고 점수 계산 (세트)
def get_highest_scores():
    all_scores = {
        "Math": set(),
        "Science": set(),
        "English": set()
    }
    
    for student in students:
        all_scores["Math"].add(student["scores"][0])
        all_scores["Science"].add(student["scores"][1])
        all_scores["English"].add(student["scores"][2])
    return {subject: max(scores) for subject, scores in all_scores.items()}
    #return {subject: scores for subject, scores in all_scores.items()} # set은 순서보장 안됨

# 예제 실행
print(get_student_info("Alice"))  # {'name': 'Alice', 'scores': (90, 85, 88)}
print(get_highest_scores())  # {'Math': 95, 'Science': 89, 'English': 92}
###############################################################################################

# 컬렉션 모듈
from collections import Counter, defaultdict

# 점수 분포 계산 (Counter)
def calculate_score_distribution():
    score_distribution = Counter()
    for student in students:
        score_distribution.update(student["scores"])
    return score_distribution

# 학생별 평균 점수 계산 (defaultdict)
def calculate_average_scores():
    average_scores = defaultdict(list)
    for student in students:
        average_scores[student["name"]].append(sum(student["scores"]) / len(student["scores"]))
    return average_scores

# 예제 실행
print(calculate_score_distribution())  # Counter({85: 3, 90: 1, 88: 1, 78: 1, 81: 1, 92: 1, 95: 1, 89: 1})
print(calculate_average_scores())  # defaultdict(<class 'list'>, {'Alice': [87.66666666666667], 'Bob': [83.66666666666667], 'Charlie': [89.66666666666667]})

cal_score = calculate_score_distribution()

for k, v in cal_score.items():
    print(f'key, value: {k}, {v}')
    

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

print(countLetters('hello world'))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(Counter('hello world').most_common())  # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

def find_max(word):
    counter = Counter(word)
    print(f'counter: {counter}')
    max_count = -1
    for letter, cnt in counter.items():
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count

print(f"{find_max('hello world')}")  # ('l', 3)


### 리스트 컴프리헨션
# 리스트 컴프리헨션을 사용하여 학생들의 이름 목록과 평균 점수 목록을 간단하게 생성합니다.

# 학생들의 이름 목록 생성
student_names = [student["name"] for student in students]
print(student_names)  # ['Alice', 'Bob', 'Charlie']

# 학생별 평균 점수 목록 생성
average_scores = [sum(student["scores"]) / len(student["scores"]) for student in students]
print(average_scores)  # [87.66666666666667, 83.66666666666667, 89.66666666666667]

# 특정 과목(예: 수학)의 최고 점수 획득 학생 목록 생성
highest_math_score = max(student["scores"][0] for student in students)
print(highest_math_score)  
top_math_students = [student["name"] for student in students if student["scores"][0] == highest_math_score]
print(top_math_students)  # ['Charlie']
