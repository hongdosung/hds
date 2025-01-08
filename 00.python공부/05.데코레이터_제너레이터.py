# 위 코드에서 my_decorator는 say_hello 함수를 감싸며, say_hello 함수 호출 전후에 추가적인 작업을 수행
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Example usage
say_hello("World")

print(f"{'='*100}\n")

# 위 코드에서 say_hello 함수는 먼저 decorator1에 의해 데코레이트되고, 그 다음 decorator2에 의해 데코레이트됩니다.
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        func(*args, **kwargs)
    return wrapper

def hds2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator1
@hds2
def say_hello(parm):
    print(f"Hello!, {parm}")

say_hello('World')

print(f"{'='*100}\n")

# @ 제너레이터
# 제너레이터는 이터레이터의 일종으로, yield 키워드를 사용하여 값을 하나씩 생성하는 함수입니다. 
# 제너레이터는 모든 값을 한 번에 메모리에 올리지 않고, 필요할 때 값을 생성하여 메모리 사용을 최적화합니다.
# 제너레이터 함수는 yield 키워드를 사용하여 값을 하나씩 반환합니다.
# [제너레이터 표현식]
# 제너레이터 표현식은 리스트 컴프리헨션과 유사한 문법을 사용하지만, 소괄호 ()를 사용하여 정의합니다. 
# 제너레이터 표현식은 메모리 효율적인 반복을 위해 사용됩니다

# 제너레이터 예제
def my_generator():
    yield 1
    yield 2
    yield 3

# Example usage
gen = my_generator()
for value in gen:
    print(value)

print(f"{'='*100}\n")


gen_exp = (x ** 2 for x in range(10))
for value in gen_exp:
    print(value)

print(f"{'='*100}\n")


def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num
        
        # if num > 1000:
        #     break

gen = infinite_sequence()
for i in range(10):
    print(next(gen))
    
print(f"{'='*100}\n")

# 다음 예제에서는 함수 실행 시간을 측정하는 데코레이터와 대용량 데이터 처리를 위한 제너레이터를 결합합니다.
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def large_data_processing():
    def data_generator(size):
        for i in range(size):
            yield i
            
    total = 0
    for value in data_generator(10**7):
        total += value
    return total

result = large_data_processing()
print(f"Total: {result}")

print(f"{'='*100}\n")