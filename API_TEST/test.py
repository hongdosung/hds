def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# 제너레이터 객체 생성
counter = count_up_to(5)
print(f'counter : {counter}')

# 제너레이터 값 하나씩 출력
for num in counter:
    print(f'제너레이터 : {num}')

    squares = (x ** 2 for x in range(1, 11))
for squ in squares:
    print(f'squares : {squ}')
#################################################

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 함수 호출
result = factorial(5)
print(result)  # 120

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(filtered_numbers)  # [6, 8, 10]

squares = (x ** 2 for x in range(1, 11))

# 제너레이터 값 하나씩 출력
for square in squares:
    print(square)
    

####################################################################################
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

# 예제 실행
print(get_student_info("Alice"))  # {'name': 'Alice', 'scores': (90, 85, 88)}
print(get_highest_scores())  # {'Math': 95, 'Science': 89, 'English': 92}



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
####################################################################################
