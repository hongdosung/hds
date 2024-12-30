
class Person:
    # 클래스 변수
    species = 'Home sapiens'
    # 생성자 메소드
    def __init__(self, *args):
        self.name = args[0]  # 인스턴스 변수
        self.age  = args[1]  # 인스턴스 변수
        
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if 0 <= age <= 120:  # 간단한 유효성 검사
            self.age = age
        else:
            raise ValueError("Invalid age")

    # 인스턴스 메소드
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    @classmethod
    def species_info(cls):
        print(f"Species: {cls.species}")
    
    @staticmethod
    def add(a, b):
        return a + b
    
    
# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 메소드 호출
person1.greet()  # Hello, my name is Alice and I am 30 years old.
person2.greet()  # Hello, my name is Bob and I am 25 years old.

# 클래스 변수 접근
print(person1.species)  # Homo sapiens
print(person2.species)  # Homo sapiens

# 인스턴스 변수 접근
print(person1.name)  # Alice
print(person2.name)  # Bob

# 클래스 메소드 호출
Person.species_info()  # Species: Homo sapiens

# 정적 메소드 호출
result = Person.add(5, 3)
print(result)  # 8


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 객체 생성 및 메소드 호출
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!

def make_animal_speak(animal):
    print(animal.speak())

#### 다형성
# make_animal_speak 함수가 Animal 클래스의 객체를 매개변수로 받아, 다형성을 이용해 Dog와 Cat 객체의 speak 메소드를 호출
make_animal_speak(dog)  # Buddy says Woof!
make_animal_speak(cat)  # Whiskers says Meow!

#### 캡슐화
# 캡슐화(Encapsulation)는 객체의 내부 상태를 외부에서 직접 접근하지 못하도록 하고, 
# 공개된 메소드를 통해서만 접근할 수 있도록 하는 개념입니다. 이를 통해 데이터의 무결성을 보호하고, 객체의 상태를 제어할 수 있습니다.


# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
print(person.get_name())  # Alice
print(person.get_age())   # 30

person.set_name("Bob")
person.set_age(120)
print(person.get_name())  # Bob
print(person.get_age())   # 25

# 직접 접근 시도 (실패)
print(person.name)  # AttributeError: 'Person' object has no attribute '__name'


class Student:
  def __init__(self, name, age):
    self._name = name
    if age <= 10:
      raise ValueError('11살 이상의 학생만 가능합니다')
    self._age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if age <= 10:
      raise ValueError('11살 이상의 학생만 가능합니다')
    self.__age = age
    

stu1 = Student('son', 20)  # ValueError 발생
#stu1 = Student('son', 8)

# __init__함수의 영향을 받지 않으므로 ValueError가 발생하지 않는다
stu1._age = 8

print(stu1._name)  # son
print(stu1._age)  # 8


class Sample():
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
    
    def get_key(self):
        return self.__c
    
obj1 = Sample()
print(obj1.a)
print(obj1._b)
print(obj1._Sample__c)
print(obj1.get_key())
print(dir(obj1))