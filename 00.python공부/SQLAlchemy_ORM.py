# SQLAlchemy는 파이썬의 대표적인 ORM(Object-Relational Mapping) 라이브러리로, 
# 데이터베이스와의 상호작용을 객체 지향적으로 처리할 수 있게 해줍니다. 

# SQLAlchemy 라이브러리를 설치합니다.
# pip install sqlalchemy
# pip install sqlalchemy[sqlite]  # SQLite 사용 시
# pip install sqlalchemy[mysql]  # MySQL 사용 시

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 연결 설정
# DATABASE_URL = "sqlite:///example.db" # SQLite 사용 시
DATABASE_URL = 'mysql+mysqlconnector://user:password@localhost/exampledb'  # MySQL 사용 시

# 데이터베이스와 연결
engine = create_engine(DATABASE_URL, echo=True)
# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 베이스 클래스 생성(데이터 모델을 정의할 때 사용)
Base = declarative_base()

# 모델 정의
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=False)
    email = Column(String, unique=True, index=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 데이터베이스 작업 예제
def create_user(db: SessionLocal, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

class UserManager:
    def __init__(self):
        self.db = SessionLocal()

    def add_user(self, name, age):
        new_user = User(name=name, age=age)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id, name, age):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.age = age
            self.db.commit()
            return user
        return None

    def delete_user(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def list_users(self):
        return self.db.query(User).all()

    def close(self):
        self.db.close()

# 세션을 이용한 예제 실행
if __name__ == "__main__":
    # 세션 생성
    db = SessionLocal()
    # 새로운 사용자 객체 생성
    new_user = create_user(db, name="John Doe", email="john.doe@example.com")
    print(f"Created user: {new_user.name}, {new_user.email}")
    db.close()

    # 예제 실행
    manager = UserManager()
    manager.add_user('Alice', 30)
    manager.add_user('Bob', 25)
    for user in manager.list_users():
        print(user.name, user.age)
    manager.update_user(1, 'Alice', 31)
    print(manager.get_user(1).name, manager.get_user(1).age)
    manager.delete_user(2)
    for user in manager.list_users():
        print(user.name, user.age)
    manager.close()
#################################################################################
  
#################################################################################
try:
    # 데이터 삽입
    new_user = User(name='Alice', age=30)
    db.add(new_user)

    # 데이터베이스에 변경 사항 반영
    db.commit()
except:
    # 오류 발생 시 롤백
    db.rollback()
    raise
finally:
    # 세션 종료
    db.close()
#################################################################################
  
#################################################################################
# 컨텍스트 매니저를 사용한 트랜잭션 관리
# SQLAlchemy는 Session 객체를 컨텍스트 매니저로 사용하여 트랜잭션을 더 간단하게 관리할 수 있습니다.

from sqlalchemy.orm import Session

# 세션 생성 및 트랜잭션 관리
with Session(engine) as session:
    with session.begin():
        new_user = User(name='Bob', age=25)
        session.add(new_user)

# 예외 처리 및 트랜잭션 관리
try:
    with Session(engine) as session:
        with session.begin():
            another_user = User(name='Charlie', age=35)
            session.add(another_user)
except:
    print("Transaction failed and has been rolled back.")
#################################################################################
  
#################################################################################
# 모델 정의
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, index=True)
    balance = Column(Integer)

Base.metadata.create_all(bind=engine)

# 트랜잭션을 사용한 송금 함수
def transfer_funds(session, from_account_id, to_account_id, amount):
    from_account = session.query(Account).filter(Account.id == from_account_id).one()
    to_account = session.query(Account).filter(Account.id == to_account_id).one()

    if from_account.balance < amount:
        raise ValueError("Insufficient funds")

    from_account.balance -= amount
    to_account.balance += amount

# 예제 실행
with Session(engine) as session:
    with session.begin():
        try:
            transfer_funds(session, from_account_id=1, to_account_id=2, amount=100)
        except ValueError as e:
            print(e)
            session.rollback()
#################################################################################
  
#################################################################################
# 프로젝트 예제: 온라인 도서 관리 시스템
# 시스템은 사용자와 도서 정보를 관리하고, 도서 대여 및 반납 기능을 제공합니다.

# 1. 데이터베이스 설정 및 연동
# SQLite 데이터베이스와 연동을 설정합니다. 프로젝트 규모에 따라 MySQL로 쉽게 전환할 수 있습니다.

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship  
from datetime import datetime, timedelta, timezone

# 데이터베이스 설정  
DATABASE_URL = 'sqlite:///library.db' # SQLite 사용 시  
# DATABASE_URL = 'mysql+mysqlconnector://user:password@localhost/librarydb'  # MySQL 사용 시  

engine = create_engine(DATABASE_URL, echo=True)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()  


# 모델 정의  
class User(Base):  
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, index=True)  
    email = Column(String, unique=True, index=True)  


class Book(Base):  
    __tablename__ = 'books'  

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, index=True)  
    author = Column(String)  
    available = Column(Integer, default=1)  


class Rental(Base):  
    __tablename__ = 'rentals'  

    id = Column(Integer, primary_key=True, index=True)  
    user_id = Column(Integer, ForeignKey('users.id'))  
    book_id = Column(Integer, ForeignKey('books.id'))  
    rented_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  
    returned_at = Column(DateTime, nullable=True)  

    user = relationship("User")
    book = relationship("Book")

# 테이블 생성  
Base.metadata.create_all(bind=engine)

# 2. 데이터 삽입 및 조회
# 사용자 및 도서 추가
def add_user(session, name, email):  
    existing_user = session.query(User).filter(User.email == email).first()  
    if existing_user:  
        print(f"User with email {email} already exists.")  
        return existing_user  
    user = User(name=name, email=email)  
    session.add(user)  
    session.commit()  
    session.refresh(user)  
    return user

def add_book(session, title, author):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

# 사용자 및 도서 조회
def get_users(session):
    return session.query(User).all()

def get_books(session):
    return session.query(Book).all()

# 예제 실행
with SessionLocal() as session:
    add_user(session, 'Alice', 'alice@example.com')
    add_user(session, 'Bob', 'bob@example.com')

    add_book(session, 'The Great Gatsby', 'F. Scott Fitzgerald')
    add_book(session, '1984', 'George Orwell')

    users = get_users(session)
    books = get_books(session)

    for user in users:
        print(user.name, user.email)

    for book in books:
        print(book.title, book.author, 'Available' if book.available else 'Not Available')
#################################################################################
  
#################################################################################
# 3. 데이터베이스 트랜잭션 관리
# 도서 대여 함수
def rent_book(session, user_id, book_id):
    book = session.query(Book).filter(Book.id == book_id, Book.available == 1).first()
    if not book:
        raise ValueError("Book is not available for rent")
    
    rental = Rental(user_id=user_id, book_id=book_id)
    book.available = 0
    session.add(rental)
    session.commit()
    session.refresh(rental)
    return rental

# 도서 반납 함수
def return_book(session, rental_id):
    rental = session.query(Rental).filter(Rental.id == rental_id, Rental.returned_at == None).first()
    if not rental:
        raise ValueError("Rental record not found or book already returned")
    
    rental.returned_at = datetime.now(timezone.utc)
    rental.book.available = 1
    session.commit()
    session.refresh(rental)
    return rental

# 예제 실행
with SessionLocal() as session:  
    try:  
        rental = rent_book(session, user_id=1, book_id=1)  
        if rental:  
            print(f"Book rented: {rental.book.title} by {rental.user.name}")  
        else:  
            print("Book is not available for rent")  

        returned_rental = return_book(session, rental.id)  
        if returned_rental:  
            print(f"Book returned: {returned_rental.book.title} by {returned_rental.user.name} at {returned_rental.returned_at}") 
        else:  
            print("Rental not found or already returned")  
    except Exception as e:  
        session.rollback()  
        print(f"Transaction failed: {e}")
#################################################################################
  
#################################################################################
# 대여 기간 제한 및 연체 처리
def enforce_rental_period(session):  
    overdue_rentals = session.query(Rental).filter(  
        Rental.returned_at == None,  
        Rental.rented_at < datetime.now(timezone.utc) - timedelta(days=30)  
    ).all()  

    for rental in overdue_rentals:
        rental.returned_at = datetime.now(timezone.utc)  
        rental.book.available = 1  

    if overdue_rentals:
        session.commit()  
        for rental in overdue_rentals:
            print(f"Overdue book returned: {rental.book.title} by {rental.user.name}")  


# 예제 실행  
with SessionLocal() as session:
    enforce_rental_period(session)
