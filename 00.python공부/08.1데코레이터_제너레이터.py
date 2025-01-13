#### 데코레이터 ####
# 데코레이터는 함수를 감싸는 함수로, 기존 함수에 추가적인 기능을 제공할 때 사용됩니다. 
# 데코레이터는 재사용 가능한 코드 블록을 작성하고, 이를 통해 코드의 가독성과 유지보수성을 높일 수 있습니다.
# 
# 데코레이터의 기본 문법
# 데코레이터는 다른 함수를 인자로 받아 새로운 함수를 반환하는 함수입니다. @데코레이터_이름 구문을 사용하여 함수를 데코레이트할 수 있습니다.

# 위 코드에서 my_decorator는 say_hello 함수를 감싸며, say_hello 함수 호출 전후에 추가적인 작업을 수행
print('#### 데코레이터 ####')
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        #func(*args, **kwargs)
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Example usage
say_hello("World")
print()

# 위 코드에서 say_hello 함수는 먼저 decorator2에 의해 데코레이트되고, 그 다음 decorator1에 의해 데코레이트됩니다.
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        func(*args, **kwargs)
        print("Decorator 11111")
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        func(*args, **kwargs)
        #result = func(*args, **kwargs)
        #return result
        print("Decorator 2222")
    return wrapper

@decorator1
@decorator2
def say_hello(parm):
    print(f"Hello222!, {parm}")

say_hello('World')

print(f"{'='*100}\n")

print('#### 제너레이터 ####')
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
# for value in gen_exp:
#     print(value)

print(f"{'='*100}\n")

# 제너레이터를 사용하여 무한 수열을 생성하는 예제입니다.
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
            print(i)
            yield i
            
    total = 0
    #for value in data_generator(10**4):
    for value in range(10**7):
        total += value
    return total

result = large_data_processing()
print(f"Total: {result}")

print(f"{'='*100}\n")