class Person:
    def __init__(self, *args):
        self.name2 = args[0]  # 인스턴스 변수
        self.__name = args[0]  # private 변수
        self.__age  = args[1]  # private 변수

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:  # 간단한 유효성 검사
            self.__age = age
        else:
            raise ValueError("Invalid age")


# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
print(person.get_name())  # Alice
print(person.get_age())   # 30

person.set_name("Bob")
person.set_age(25)
print(person.get_name())  # Bob
print(person.get_age())   # 25

# 직접 접근 시도 (실패)
#print(person.__name)  # AttributeError: 'Person' object has no attribute '__name'
print(person.name2) 


# 위 코드에서는 Person 클래스의 __name과 __age 변수를 private 변수로 정의하고, 
# getter와 setter 메소드를 통해서만 접근할 수 있도록 하여 캡슐화를 구현합니다.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
    
    def __repr__(self):
        return f"Person(name1={self.name!r}, age1={self.age!r})"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
print(f'kkk: {person}')  # Alice, 30
print(repr(person))  # Person(name='Alice', age=30)

# 객체 생성 및 메소드 호출
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(person1 == person2)  # True