### Numpy ###
# Numpy는 고성능 수치 계산을 위한 라이브러리로, 다차원 배열 객체와 다양한 수학 함수를 제공합니다.
# pip install numpy

import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print(f"1D array: {array_1d}")

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", array_2d)

# Perform basic operations
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
max_value = np.max(array_1d)
min_value = np.min(array_1d)

print("Sum:", sum_array)
print("Mean:", mean_array)
print("Max:", max_value)
print("Min:", min_value)

# Reshape the array
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped array:\n", reshaped_array)

# Create an array of zeros
zeros_array = np.zeros((3, 3))
print("Array of zeros:\n", zeros_array)

# Create an array of ones
ones_array = np.ones((2, 4))
print("Array of ones:\n", ones_array)

# Create an identity matrix
identity_matrix = np.eye(3)
print("Identity matrix:\n", identity_matrix)


# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")

# 다차원 배열 생성
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix:\n{matrix}")

# 배열 연산
arr_sum = np.sum(arr)
print(f"Sum of array: {arr_sum}")

matrix_mean = np.mean(matrix, axis=0)
print(f"Mean of each column in matrix: {matrix_mean}")

# 배열 슬라이싱
arr_slice = arr[1:4]
print(f"Array slice: {arr_slice}")

print(f"{'='*80}\n")

# 행렬곱 함수
# 1차원 x 1차원
a = np.array([1, 3, 5])
b = np.array([4, 2, 1])
print(np.dot(a, b)) # 결과 : 1*4 + 3*2 + 5*1 = 4 + 6 + 5 = 15

# 선형 대수 연산, 2차원인 경우, 행렬곱이 수행
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print(f"Matrix product:\n{matrix_product}")

# 난수 생성
random_array = np.random.rand(3, 3)
print(f"Random array:\n{random_array}")
