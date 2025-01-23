### Pandas ###
# Pandas 데이터프레임을 생성하고 기본적인 데이터 조작을 수행

# pip install pandas

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")

# 열 선택
names = df['Name']
print(f"Names:\n{names}")

# 조건 필터링
age_above_30 = df[df['Age'] > 30]
print(f"Age above 30:\n{age_above_30}")

# 새로운 열 추가
df['Salary'] = [70000, 80000, 90000, 100000]
print(f"DataFrame with Salary:\n{df}")

# 그룹화  
grouped = df.groupby('City').mean(numeric_only=True)  
print(f"Grouped by City:\n{grouped}")  

# 데이터 병합  
data1 = {'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]}  
data2 = {'Key': ['A', 'B', 'D'], 'Value2': [4, 5, 6]}  
df1 = pd.DataFrame(data1)  
df2 = pd.DataFrame(data2)  
merged_df = pd.merge(df1, df2, on='Key', how='outer')  
print(f"Merged DataFrame:\n{merged_df}")

# 예제: 타이타닉 데이터 분석
import pandas as pd
import numpy as np

print(f"{'='*80}\n")
# 데이터 로드
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# 데이터 미리보기
print(titanic_df.head())

# 데이터 요약
print(titanic_df.describe())

# 결측값 처리
titanic_df = titanic_df.fillna(0)

# 특정 열 선택
age_and_fare = titanic_df[['Age', 'Fare']]
print(age_and_fare.head())

# 새로운 열 추가
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
print(titanic_df.head())

# 성별로 그룹화하여 생존률 계산
gender_survival_rate = titanic_df.groupby('Sex')['Survived'].mean()
print(gender_survival_rate)

# 특정 조건 데이터 필터링
children = titanic_df[titanic_df['Age'] < 18]
print(children.head())
